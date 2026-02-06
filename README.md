# Virtual Investment Committee (Agentic AI POC)

A professional-grade, multi-agent AI system built with **CrewAI** to provide deep financial analysis and investment recommendations.

## 🚀 Overview
The system employs a team of specialized AI agents representing different expertises:
- **Fundamental Analyst**: Experts in balance sheets and intrinsic valuation.
- **Technical Analyst**: Masters of price action and historical trends.
- **Sentiment Analyst**: NLP experts tracking news and market psychology.
- **Committee Chair**: Synthesizes all data into a high-conviction recommendation.

## 🛠️ Tech Stack
- **Framework**: CrewAI (Python SDK)
- **Language**: Python 3.11+
- **Configuration & Validation**: Pydantic v2 / Pydantic-Settings
- **Data Sources**: Yahoo Finance (yfinance), Serper (Google Search)
- **Dependency Management**: Poetry

## ⚙️ Setup

### 1. Prerequisites
- [Poetry](https://python-poetry.org/docs/#installation) installed.
- API keys for OpenAI (or your preferred LLM) and Serper.

### 2. Installation
```bash
# Install dependencies
poetry install
```

### 3. Configuration
Copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```

### 4. Running the Agent
```bash
poetry run python -m src.main --stock AAPL
```

## 🏗️ Project Structure
```text
investment_crew/
├── src/
│   ├── agents/          # Agent personas & logic
│   ├── tools/           # Financial & search tool wrappers
│   ├── models/          # Structured output definitions (Pydantic)
│   ├── config/          # App settings & logging
│   └── main.py          # Orchestration entry point
├── tests/               # Automated tests
└── pyproject.toml       # Environment & dependencies
```

## 📈 Roadmap
- [ ] **Step 4**: Dockerize the application.
- [ ] **Step 5**: Implement Kubernetes/Helm charts.
- [ ] **Step 6**: Infrastructure as Code (Terraform/CDK).

## ⚠️ Troubleshooting
If you encounter a `TOMLError` (e.g., `Unexpected character: u'.'`) during `poetry install`, it is likely due to a minor bug in `pybase64` dependencies on some macOS versions. 

**Fix**: Install dependencies directly into your virtualenv:
```bash
poetry run pip install "crewai[tools]" langchain-google-genai pydantic-settings yfinance python-dotenv
```

## 📄 License
MIT
