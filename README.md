# NexusSignal-Agentic-Systems

Multi-agent lead auditing and tech migration system built with Gemini 1.5 and Python
Signal-Based B2B Lead Generation & Technical Audit PipelineNexusSignal is an end-to-end Agentic AI System designed to identify high-intent B2B prospects by detecting technical "migration signals." 

Moving beyond generic outreach, this system scans mid-market sectors (Manufacturing, Exports, Logistics) to identify legacy tech debt and generates human-grade, architect-level pitches for founders.

📂 Repository StructurePlaintextNexusSignal-Agentic-System/
├── src/               # Core Agent Logic (The Engine)
├── research/          # API Experiments & Model Comparisons (Gemini 1.5 vs 2.0)
├── data/              # Final Audits, Database Backups, and Master Reports
├── leads.db           # SQLite Central Intelligence
├── .env               # API Credentials (Excluded via .gitignore)
└── README.md



🛠️ Technical WorkflowThe system operates as a sequential pipeline, transforming raw market data into high-conversion sales opportunities:Lead Ingestion (fetch_live_leads.py): Targets "Practical" Indian SMBs (20-100 employees) in major industrial hubs using the Apollo API.Technical Audit (detect_tech_free.py): Scans for "Pain Signals"—legacy tech, slow mobile response, or site downtime.Multi-Channel Enrichment (find_contacts.py): A waterfall agent leveraging Snov.io, Hunter.io, and Apollo.io to secure direct Founder/MD contact details.Humanized Pitch Engine (generate_pitches.py): Uses Gemini 1.5 Flash to draft peer-to-peer technical roadmaps, strictly avoiding "AI-isms" or sales fluff.Master Consolidation (final_consolidator.py): Generates a styled, dashboard-grade Excel report with automated outreach tiering.📊 Final Project MetricsMetricAchievementTotal Audit Pool98+ Targeted Mid-Market FirmsElite GOLD Leads25+ (Verified Founders/MDs)Direct Reach (P1)43 High-priority phone numbersOutreach Ready (P2)55 Email-verified leadsPrimary PersonaSenior Solutions Architect🏅 The "Grand Master" ArtifactThe system produces the NexusSignal_Master_Audit_2026.xlsx, a color-coded dashboard:🏅 GOLD: Elite targets with full contact density and custom pitches.📒 YELLOW: Verified direct leads for technical modernization.📘 BLUE: Growth-stage audits for long-term nurturing.🚀 How to RunBash# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup Environment Variables
# Create a .env file with your APOLLO_API_KEY, HUNTER_API_KEY, SNOV_API_KEY, and GOOGLE_API_KEY

# 3. Execute Pipeline
# Step 1: Ingest raw data from live sources
python src/fetch_live_leads.py

# Step 2: Detect technology stacks using agentic reasoning
python src/detect_tech_free.py

# Step 3: Tool-calling agent to retrieve contact information
python src/find_contacts.py

# Step 4: Generate personalized, RAG-based migration pitches
python src/generate_pitches.py

# Step 5: Final logic agent for data consolidation and cleanup
python src/final_consolidator.py

Key Highlights
Hyper-Practical Targeting: Pivoted from "Unicorns" to traditional mid-market firms where technical debt is high and engineering bandwidth is low.

Zero "Bot-Speak": Engineered a system prompt that mirrors a Senior Architect's tone, using peer-to-peer technical consultation instead of sales templates.

Fail-Safe Logic: Implemented a template fallback engine to ensure 100% pitch coverage despite API or quota limitations.
