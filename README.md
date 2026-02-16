# NexusSignal-Agentic-Systems

Autonomous B2B Technical Intelligence and Outreach Engine

NexusSignal is an end-to-end Agentic System designed to identify high-intent Ecommerce and Retail startups, audit their technical debt, and generate architect-level outreach pitches. Instead of using generic templates, this system identifies specific legacy "Pain Signals" to initiate modernization-focused conversations.

## The 4-Phase Architecture

The system operates as a sequential pipeline to ensure data integrity and reliability.

1. Phase One: Lead Fetch (fetch_live_leads.py)
Goal: Sourcing raw startup data in Growth Hubs like Bengaluru and Mumbai.
Tech: Apollo.io API.
2. Phase Two: Tech Audit (detect_tech_free.py)
Goal: Identifying Modernization opportunities.
Tech: Python (Requests and RegEx).
3. Phase Three: Enrichment (find_contacts.py)
Goal: Waterfall discovery of Founder and MD contact information.
Tech: Snov.io and Hunter.io.
4. Phase Four: Finalize (master_finalizer.py)
Goal: AI Pitch Generation and Master Reporting.
Tech: Gemini 2.0 Flash.

## The Tech Stack

Intelligence (AI):

* Official Google AI SDK (google-generativeai): Integrated directly for zero-overhead execution and native access to Gemini features.
* Gemini 2.0 Flash: Serves as the Reasoning Engine to generate 3-sentence, sales-fluff-free pitches.

Data Discovery (Waterfall Strategy):

* Apollo.io: Broad market sector searches and founder identification.
* Snov.io: Primary source for verified company phone numbers.
* Hunter.io: Final verification layer for professional emails.

Core Infrastructure:

* Database: SQLite (leads.db) for local storage on the D: Drive.
* Orchestration: Python-native pipeline designed for maximum execution speed without heavy framework abstractions.

## Project Structure

To optimize performance, the project utilizes a cross-drive architecture:

C:/ (Source and Logic)

* src/: Core Logic (find_contacts.py, master_finalizer.py)
* research/: Benchmark scripts (test_gemini.py)
* NexusSignal_Master_Audit_2026.xlsx: Final Deliverable

D:/ (Data and Execution)

* leads.db: Central SQLite Intelligence
* fetch_live_leads.py: Pipeline Entry Point
* detect_tech_free.py: Technical Scanner
* .env: Centralized API Secret Storage

## Unique Value Proposition

* No-Fluff Policy: System prompts strictly prohibit AI-isms like "Unlock" or "Leverage."
* Precision Filtering: Targets startups with 10-50 employees where decision-makers are technical and accessible.
* Zero-Framework Overhead: Using the native SDK achieves low latency and high reliability on local hardware.
* Waterfall Logic: If one API fails to find a contact, the system automatically triggers the next one in the sequence.

## Performance Metrics

* Total Audit Pool: 98 Targeted Mid-Market Firms.
* Elite GOLD Leads: 25 Verified Founders with high modernization needs.
* Direct Reach: 43 Leads with direct-dial phone numbers.
* AI Efficiency: 100 percent pitch coverage using Gemini 2.0.

## Execution Pipeline

Run the full workflow in sequence:

1. python D:/fetch_live_leads.py
2. python D:/detect_tech_free.py
3. python C:/src/find_contacts.py
4. python C:/src/master_finalizer.py

