# NexusSignal-Agentic-Systems
NexusSignal is an end-to-end Agentic AI System designed to identify high-intent B2B prospects by detecting technical "migration signals". Moving beyond generic outreach, this system scans mid-market sectors (Manufacturing, Exports, Logistics) to identify legacy tech debt and generates human-grade, architect-level pitches for founders.

NexusSignal-Agentic-System/
├── src/          # Core Agent Logic (The Engine)
├── research/     # API Experiments & Model Comparisons (Gemini 1.5 vs 2.0)
├── data/         # Final Audits, Database Backups, and Master Reports
├── leads.db      # SQLite Central Intelligence
├── .env          # API Credentials (Excluded via .gitignore)
└── README.md     # Documentation & Systems Thinking

Technical Workflow
The system operates as a sequential pipeline, transforming raw market data into high-conversion sales opportunities:

Lead Ingestion (fetch_live_leads.py): Targets "Practical" Indian SMBs (20-100 employees) in major industrial hubs using the Apollo API.

Technical Audit (detect_tech_free.py): Scans for "Pain Signals"—legacy tech, slow mobile response, or site downtime.

Multi-Channel Enrichment (find_contacts.py): A waterfall agent leveraging Snov.io, Hunter.io, and Apollo.io to secure direct Founder/MD contact details.

Trade-offs & Decisions (Non-Negotiable)In line with the hiring philosophy, this project prioritizes Reliability and Systems Thinking:Cost vs. Accuracy: Utilized Gemini 1.5 Flash for high-volume pitch generation to minimize latency while reserving Gemini 1.5 Pro for the complex technical audit phase.Fail-Safe Logic: Implemented a template fallback engine to ensure 100% pitch coverage despite API or quota limitations.Agentic Tone: Engineered system prompts to mirror a Senior Architect's tone, focusing on technical consultation instead of sales templates.

📊 Final Project MetricsMetricAchievementTotal Audit Pool98+ Targeted Mid-Market FirmsElite GOLD Leads25+ (Verified Founders/MDs)Direct Reach (P1)43 High-priority phone numbersOutreach Ready (P2)55 Email-verified leads🚀 Execution PipelineTo run the full agentic workflow, execute the following commands in order:Bash
# 1. Install dependencies 
pip install -r requirements.txt

# 2. Execute the sequential Agent steps
python src/fetch_live_leads.py
python src/detect_tech_free.py
python src/find_contacts.py
python src/generate_pitches.py
python src/final_consolidator.py

🏅 The "Grand Master" ArtifactThe system produces NexusSignal_Master_Audit_2026.xlsx, a color-coded dashboard:GOLD: Elite targets with full contact density and custom pitches.YELLOW: Verified direct leads for technical modernization.BLUE: Growth-stage audits for long-term nurturing.

Humanized Pitch Engine (generate_pitches.py): Uses Gemini 1.5 Flash to draft peer-to-peer technical roadmaps, strictly avoiding "AI-isms" or sales fluff.

Master Consolidation (final_consolidator.py): Generates a styled, dashboard-grade Excel report with automated outreach tiering.
