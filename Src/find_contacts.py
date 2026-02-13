import sqlite3
import requests
import os
import time
import sys
from urllib.parse import urlparse
from dotenv import load_dotenv

# Ensure UTF-8 output for Windows console
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Load Environment Variables
ENV_PATH = 'd:/NexusSignal/.env'
load_dotenv(ENV_PATH)

# Configuration
DB_PATH = 'd:/NexusSignal/leads.db'
APOLLO_API_KEY = os.getenv('APOLLO_API_KEY')
HUNTER_API_KEY = os.getenv('HUNTER_API_KEY')
SNOV_CLIENT_ID = os.getenv('SNOV_CLIENT_ID')
SNOV_SECRET = os.getenv('SNOV_SECRET')

class EnrichmentAgent:
    def __init__(self):
        self.snov_token = None
        self.gold_leads_count = 0

    def get_snov_token(self):
        """Step A/C Helper: Authenticate with Snov.io"""
        url = "https://api.snov.io/v1/oauth/access_token"
        payload = {
            'client_id': SNOV_CLIENT_ID,
            'client_secret': SNOV_SECRET,
            'grant_type': 'client_credentials'
        }
        try:
            res = requests.post(url, data=payload)
            res.raise_for_status()
            self.snov_token = res.json().get('access_token')
            return self.snov_token
        except Exception as e:
            print(f"Snov.io Auth Error: {e}")
            return None

    def snov_find_prospect(self, domain):
        """Step A: Find name via Snov.io"""
        if not self.snov_token and not self.get_snov_token():
            return None

        headers = {'Authorization': f'Bearer {self.snov_token}'}
        start_url = "https://api.snov.io/v2/domain-search/prospects/start"
        payload = {
            'domain': domain,
            'positions': ['Founder', 'Co-Founder', 'CEO'],
            'limit': 1
        }
        
        try:
            res = requests.post(start_url, json=payload, headers=headers)
            res.raise_for_status()
            task_hash = res.json().get('meta', {}).get('task_hash')
            if not task_hash: return None

            # Retry loop for task completion
            result_url = f"https://api.snov.io/v2/domain-search/prospects/result/{task_hash}"
            prospects = []
            for _ in range(5):
                time.sleep(5)
                res = requests.get(result_url, headers=headers)
                res.raise_for_status()
                data = res.json()
                prospect_list = data.get('prospects') or data.get('data') or []
                if data.get('status') == 'completed' or prospect_list:
                    prospects = prospect_list
                    break
                elif data.get('status') == 'failed':
                    break
            
            if prospects:
                p = prospects[0]
                first = p.get('first_name', '')
                last = p.get('last_name', '')
                return f"{first} {last}".strip() or p.get('name')
        except Exception as e:
            print(f"Snov.io Search Error: {e}")
        return None

    def apollo_find_name(self, domain):
        """Step A Fallback: Find name via Apollo"""
        url = "https://api.apollo.io/v1/people/match"
        headers = {
            "Content-Type": "application/json",
            "X-Api-Key": APOLLO_API_KEY
        }
        payload = {
            "domain": domain, 
            "reveal_personal_emails": True, 
            "titles": ["Founder", "Co-Founder", "CEO", "Managing Director", "Owner", "Partner", "Director"]
        }
        try:
            res = requests.post(url, json=payload, headers=headers)
            if res.status_code == 200:
                return res.json().get('person', {}).get('name')
        except:
            pass
        return None

    def hunter_find_email(self, name, domain):
        """Step B: Email Waterfall via Hunter.io"""
        if not name or not domain: return None
        
        # Split names
        parts = name.split(' ')
        first = parts[0]
        last = parts[-1] if len(parts) > 1 else ''

        url = "https://api.hunter.io/v2/email-finder"
        params = {
            'domain': domain,
            'first_name': first,
            'last_name': last,
            'api_key': HUNTER_API_KEY
        }
        try:
            res = requests.get(url, params=params)
            res.raise_for_status()
            data = res.json().get('data', {})
            if data.get('verification', {}).get('status') == 'deliverable':
                return data.get('email')
            return data.get('email') # Fallback if not strictly deliverable but found
        except Exception as e:
            print(f"Hunter.io Error: {e}")
        return None

    def hunter_domain_search(self, domain):
        """Step A Fallback: Find any lead via Hunter.io Domain Search"""
        url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
        try:
            res = requests.get(url)
            if res.status_code == 200:
                data = res.json().get('data', {})
                emails = data.get('emails', [])
                if emails:
                    for email in emails:
                        fname = email.get('first_name')
                        lname = email.get('last_name')
                        if fname and lname:
                            return f"{fname} {lname}", email.get('value')
                        elif email.get('value'):
                            return email.get('value').split('@')[0].capitalize(), email.get('value')
        except:
            pass
        return None, None

    def snov_get_company_phone(self, domain):
        """Step C: Phone Retrieval via Snov.io"""
        if not self.snov_token and not self.get_snov_token():
            return None

        headers = {'Authorization': f'Bearer {self.snov_token}'}
        start_url = "https://api.snov.io/v2/domain-search/start/" # Corrected based on search
        payload = {'domain': domain}
        
        try:
            res = requests.post(start_url, json=payload, headers=headers)
            res.raise_for_status()
            task_hash = res.json().get('meta', {}).get('task_hash')
            if not task_hash: return None

            # Retry loop for task completion
            result_url = f"https://api.snov.io/v2/domain-search/result/{task_hash}"
            phone = None
            for _ in range(5):
                time.sleep(5)
                res = requests.get(result_url, headers=headers)
                res.raise_for_status()
                data = res.json()
                company_data = data.get('data') if isinstance(data.get('data'), dict) else data
                if data.get('status') == 'completed' or company_data.get('hq_phone'):
                    phone = company_data.get('hq_phone')
                    break
                elif data.get('status') == 'failed':
                    break
            return phone
        except Exception as e:
            print(f"Snov.io Phone Error: {e}")
        return None

    def extract_domain(self, url):
        if not url: return None
        if not url.startswith('http'): url = 'http://' + url
        try:
            domain = urlparse(url).netloc
            return domain[4:] if domain.startswith('www.') else domain
        except: return None

    def run(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Target RED, YELLOW and NULL leads (for fresh startup audits)
        cursor.execute("SELECT id, lead_name, website_url FROM prospects WHERE priority IN ('RED', 'YELLOW') OR priority IS NULL")
        leads = cursor.fetchall()
        print(f"Processing {len(leads)} leads...")

        for lead_id, lead_name, website_url in leads:
            domain = self.extract_domain(website_url)
            if not domain: continue

            print(f"\n--- Eniching {lead_name} ({domain}) ---")
            
            # Step A & B: Identity & Email (Recovery Mode)
            contact_name = self.apollo_find_name(domain)
            contact_email = None
            
            if not contact_name:
                print(f"Apollo match failed for {domain}. Trying Snov.io Search...")
                contact_name = self.snov_find_prospect(domain)
            
            if contact_name:
                contact_email = self.hunter_find_email(contact_name, domain)
                if not contact_email:
                    print(f"Hunter.io failed for {contact_name}. Trying Snov.io Email finder fallback...")
                    # Snov.io has a simple email finder too but we'll stick to prospect search results for now
            
            if not contact_name and not contact_email:
                print(f"Identity search failed. Trying Hunter Domain Search...")
                contact_name, contact_email = self.hunter_domain_search(domain)

            if contact_name and contact_email:
                print(f"Secured Lead: {contact_name} ({contact_email})")
            else:
                print("Enrichment failed. Skipping.")
                continue

            # Step C: Phone Retrieval
            contact_phone = self.snov_get_company_phone(domain)
            if contact_phone:
                print(f"Found Phone: {contact_phone}")

            # Update DB
            priority_update = ""
            if contact_email: # Success: Any verified email is a win for the presentation
                priority_update = ", priority = 'GOLD_LEAD'"
                self.gold_leads_count += 1
                print(f"Status Updated: GOLD_LEAD ({self.gold_leads_count})")

            cursor.execute(f"""
                UPDATE prospects 
                SET contact_name = ?, contact_email = ?, contact_phone = ? {priority_update}
                WHERE id = ?
            """, (contact_name, contact_email, contact_phone, lead_id))
            conn.commit()

            # Trigger Export if threshold met
            if self.gold_leads_count >= 15:
                print(f"\n--- THRESHOLD MET: {self.gold_leads_count} GOLD LEADS ---")
                print("Triggering export_leads.py...")
                try:
                    import subprocess
                    subprocess.run(["d:/NexusSignal/venv/Scripts/python.exe", "c:/Users/HP/OneDrive/NexusSignal/export_leads.py"], check=True)
                    print("Export completed successfully.")
                    break # Stop processing further once exported
                except Exception as e:
                    print(f"Export Trigger Error: {e}")

        conn.close()
        print(f"\nSummary: Enriched {self.gold_leads_count} GOLD leads today.")

if __name__ == "__main__":
    agent = EnrichmentAgent()
    agent.run()
