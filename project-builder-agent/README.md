# AI Project Builder Agent 🤖

> Turn any job description into a production-ready AI/ML project in seconds

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 What It Does

Paste a job description → Get a complete, role-specific AI project with:
- ✅ **Real-world problem scenario** with business ROI
- ✅ **Production-ready code** (FastAPI backend, React frontend optional)
- ✅ **Sample data generators** to test immediately
- ✅ **Deployment configs** (Docker, Kubernetes)
- ✅ **Comprehensive documentation** (README, ARCHITECTURE, scenarios)

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+ (for frontend)
- Docker (optional)

### Local Setup

**Option 1: One-Click Startup** ⭐
```bash
# Double-click START_ALL.bat (Windows)
# This starts both backend and frontend automatically
```

**Option 2: Manual**
```bash
# Terminal 1 - Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Terminal 2 - Frontend  
cd frontend
npm install
npm run dev
```

Then open: **http://localhost:5173**

## 📊 Example Outputs

### Input
```
Job Description: "Seeking Senior AI Developer for agentic AI platform.
Multi-agent orchestration, LLM integration (GPT-4, Claude), RAG required."
```

### Output
```
📁 enterprise_agentic_ai_platform_a1b2c3/
├── src/
│   ├── agents/orchestrator.py      # Multi-agent coordinator
│   ├── api/main.py                 # FastAPI application
│   └── core/llm_client.py          # OpenAI + Anthropic integration
├── data/sample_tickets.json        # Real test data
├── deployments/
│   ├── kubernetes/                 # K8s manifests with GPU support
│   └── docker/Dockerfile           # Production container
├── PROJECT_SCENARIO.md             # Business case: $210K ROI
├── README.md                       # Full documentation
└── ARCHITECTURE.md                 # Technical deep-dive
```

## 💡 Features

- **Context-Aware**: Detects seniority (Junior/Mid/Senior) and adjusts complexity
- **Domain Detection**: Automatically identifies CV, NLP, MLOps, Agentic AI, etc.
- **Tech Stack Matching**: Includes Kubernetes if mentioned, NVIDIA for GPU jobs, etc.
- **Business-Driven**: Every project solves a real $X problem with measurable ROI
- **Sample Data**: Includes working data generators (transactions, support tickets, etc.)

## 🏗️ Project Types Generated

| Domain | Generated Project | Example ROI |
|--------|-------------------|-------------|
| Agentic AI | Customer Support Automation | $210K/year savings |
| MLOps | E-Commerce Fraud Detection | $2.6M prevented loss |
| NLP + RAG | Enterprise Knowledge Search | $400K productivity gain |
| Computer Vision | Manufacturing Defect Detection | $425K savings |

## 🛠️ Tech Stack

**Backend:**
- Python 3.10+
- FastAPI (API framework)
- Pydantic (validation)

**Frontend:**  
- React 18
- Vite (build tool)
- Lucide React (icons)

**Generated Projects Include:**
- PyTorch / TensorFlow
- OpenAI / Anthropic APIs
- LangChain (for agentic AI)
- Docker + Kubernetes
- MLflow (MLOps)

## 📖 Documentation

- [Quick Start Guide](QUICK_START.md)
- [Project Ideas](PROJECT_IDEAS.md) - 5 real-world project ideas to build
- [Upgrade Notes](UPGRADE_NOTES.md)

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📝 License

MIT License - feel free to use for your portfolio projects!

## 🌟 Star History

If this helped you land an interview, please star this repo! ⭐

---

**Built with ❤️ to help developers showcase their skills**
