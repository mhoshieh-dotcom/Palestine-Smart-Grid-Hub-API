### 🇵🇸 Palestine Smart Grid Hub API (Enterprise Backend Server)

An advanced, production-grade Web API and centralized backend control server designed for the automation, monitoring, and AI-driven diagnosis of independent power generation stations across Palestine. 

This project bridges **Electrical Engineering logic** with dynamic web architectures, utilizing a rock-solid relational database and the latest 2026 Generative AI models to conduct real-time structural audits and prevent cascading blackouts. 

### ⚡ Architectural Blueprint & System Data Flow

The system follows a scalable, decoupled microservices structure compliant with modern industry standards: 

1. **API Routing & Network Framework:** Built on **FastAPI**, handling high-throughput asynchronous web requests and validating payload payloads securely via **Pydantic Schemas**.
2. **Persistent Storage Layer:** Connected permanently to a localized **PostgreSQL** database instances using **SQLAlchemy ORM**, executing clean transactions without hardcoded script dependencies.
3. **Cryptographic Identity Control (Authentication):** Implements modern password salting and hashing utilizing native byte-level **Bcrypt** algorithms, preventing brute-force access to critical utility grid configurations.
4. **AI Diagnostics Infrastructure:** Integrated with Google's state-of-the-art **Gemini 3.8 Flash Engine** via the modern google-genai SDK, streaming live database summaries for deterministic fault estimation.

### 🚀 Key System Capabilities (CRUD & Business Logic)

* **Relational Power Distribution Tracking (GET /stations):** Fetches live status parameters (megawatts capacity, city deployment, operational grid health) natively from active relational database tuples.
* **Secured Remote Sign-Up & Token Verification (POST /signup & /login):** Encrypts operator credentials inside PostgreSQL and delivers encrypted authorization web payloads.
* **The Station Decommission Safeguard (DELETE /decommission-station/{name}):** An automated safety relay route that prevents operators from deleting critical grid nodes if their active operational status is flagged as "Active", raising protective HTTP Exceptions.
* **Full Grid Emergency Clearance (DELETE /reset-grid):** An authorized database broadcast command that purges memory blocks using transaction safeguards during catastrophic system overrides.
* **The Autonomous Real-Time Grid Audit (POST /ai/analyze-db-load):** Automates grid diagnostics. The backend queries the database, formats the layout, and feeds it into the Gemini 3.8 model to generate live advisory recommendations covering local utility metrics (such as JDECO, GEDCO, NEDCO networks).

### 🛠️ The Professional Technical Stack

* **Language:** Python 3.14+
* **Framework:** FastAPI (Asynchronous ASGI server architecture)
* **Database Driver & ORM:** PostgreSQL + SQLAlchemy + Psycopg (Binary Bundle)
* **Information Security:** Native Bcrypt Hashing & PyJWT Tokens
* **Artificial Intelligence Engine:** Google Gemini 3.8 Flash API

### 📊 Live Sample AI Diagnostic Output

When the automated database audit endpoint is executed, the AI engine processes live transmission line limits and delivers highly-specialized SCADA-level technical assessments like the following: 

json

{
  "status": "Success",
  "source": "PostgreSQL Live Database",
  "engineering_analysis_report": "### Grid Telemetry & Operational Analysis\n* Total Active Capacity: 900 MW\n* Detected Vulnerabilities: Severe N-1 Contingency Violation at Jenin Node (Accounts for 50% of active grid power).\n\n### Technical Recommendations to Prevent Blackouts\n1. Synchronize Jericho (20 MW) immediately as an Operating Spinning Reserve to offset reactive power deficits.\n2. Arm directional Under-Frequency Load Shedding (UFLS) relays configured at 49.2 Hz at high-density nodes.\n3. Accelerate Nablus maintenance corridors to eliminate northern transmission bottlenecks."
}

Use code with caution.

### ⚙️ Installation & Local Feeder Setup

To clone and execute this utility server on your local machine, run the following commands sequentially inside your terminal: 

bash

# 1. Clone the repository framework
git clone https://github.com/YOUR_USERNAME/Palestine-Smart-Grid-Hub-API.git
cd Palestine-Smart-Grid-Hub-API

# 2. Install the production-ready packages and connectors
pip install fastapi[standard] sqlalchemy psycopg[binary] bcrypt pyjwt google-genai

# 3. Spin up the Uvicorn web reloader engine
python -m uvicorn main:app --reload

Use code with caution.

Once initialized, navigate to http://127.0.0.1:8000/docs on your browser to view the fully interactive Swagger UI management console dashboard.
