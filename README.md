# NexusSignal-Agentic-Systems
An Agentic AI System that finds technical debt and generates 1-on-1 sales pitches.

NexusSignal isn't a scraper; it’s a Senior Solutions Architect in a box. It scans the web for Indian ecommerce startups (10-50 employees), identifies outdated tech stacks (like legacy PHP or Magento), and drafts professional pitches to help them modernize. 
The 4-Step Pipeline
The system runs as a sequential engine to ensure 100% data accuracy.
Lead Fetch (Apollo API): Sources high-growth startups in Bengaluru, Mumbai, and Gurgaon.
Tech Audit : Detects "Pain Signals" like slow site speeds or legacy infrastructure.
Enrichment (Waterfall API): Uses Snov.io and Hunter.io to find verified Founder/CTO contact info.
AI Pitch (Gemini 2.0 Flash): Generates 3-sentence, "no-fluff" pitches tailored to their specific tech debt.

The Stack
Brain: Google Gemini 2.0 Flash (Native Python SDK — No LangChain overhead).
Data: SQLite (leads.db) & Pandas for Excel reporting.
Intelligence: Apollo, Snov.io, and Hunter.io for multi-layer verification.

Project Structure
├── src/             # Master Engine & Pitch Generator
├── research/        # Model benchmarks (Gemini 1.5 vs 2.0)
├── data/            # Final Excel Audits & SQLite DB
└── .env             # API Keys (Protected)

Results at a Glance
Metric,Achievement
Total Audit Pool,98+ Mid-Market Firms
Elite GOLD Leads,25+ (Verified Founders + Tech Debt)
Direct Reach,43 Leads with verified phone numbers
AI Efficiency,100% Pitch coverage (Zero fluff))

Quick Start
Bash# Install requirements
pip install -r requirements.txt

# Run the pipeline
python D:/fetch_live_leads.py
python D:/detect_tech_free.py
python C:/src/find_contacts.py
python C:/src/master_finalizer.py

Unique ValueWaterfall Logic: If one API fails to find a contact, the system automatically triggers the next.Zero-Fluff AI: Banned words like "Unlock" or "Leverage" to ensure pitches sound human.
