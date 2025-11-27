class DocGenerator:
    def generate(self, analysis: dict, project_type: str) -> dict:
        """
        Generates comprehensive, role-specific README.md and ARCHITECTURE.md.
        """
        tech_stack_str = ", ".join(analysis["tech_stack"])
        business_goal = analysis["business_goal"]
        domain = analysis.get("domain", "ml")
        seniority = analysis.get("seniority", "mid")
        key_requirements = analysis.get("key_requirements", [])
        
        # Generate tailored README
        readme = self._generate_readme(analysis, project_type, tech_stack_str, business_goal, domain, seniority, key_requirements)
        
        # Generate detailed architecture doc
        architecture = self._generate_architecture(analysis, project_type, tech_stack_str, domain)
        
        return {
            "README.md": readme,
            "ARCHITECTURE.md": architecture
        }
    
    def _generate_readme(self, analysis, project_type, tech_stack_str, business_goal, domain, seniority, key_requirements):
        """Generate a comprehensive, impressive README."""
        
        readme = f"""# {business_goal.title() if business_goal else 'AI Solution Platform'}

## 🎯 Executive Summary

This project directly addresses the requirement: **"{business_goal}"**

Built with an enterprise-grade tech stack ({tech_stack_str}), this solution demonstrates:
- ✅ Production-ready architecture with scalability and security built-in
- ✅ Industry best practices for {domain.upper()} deployment
- ✅ Full lifecycle implementation: data → training → deployment → monitoring
- ✅ Comprehensive testing and CI/CD pipeline

## 🏗️ Architecture Overview

This is a **{seniority}-level** implementation showcasing:
"""
        
        if project_type == "agentic_platform_enterprise":
            readme += """
### Multi-Agent Orchestration System
- **Agent Coordinator**: Decomposes complex tasks and routes to specialized agents
- **LLM Integration**: Supports OpenAI, Anthropic, and local models
- **API Layer**: FastAPI-based REST API for agent interactions
- **Frontend Dashboard**: React-based UI for task management and monitoring

### Key Components
1. **`src/agents/orchestrator.py`**: Multi-agent task orchestration
2. **`src/core/llm_client.py`**: Multi-provider LLM client (OpenAI, Anthropic, Llama)
3. **`src/api/main.py`**: FastAPI application with REST endpoints
4. **`frontend/src/AgentDashboard.jsx`**: React dashboard for agent monitoring
"""
        elif project_type == "mlops_pipeline":
            readme += """
### MLOps/LLMOps Pipeline
- **Training Pipeline**: Automated training with experiment tracking (MLflow)
- **Model Registry**: Centralized model versioning and deployment
- **CI/CD**: GitHub Actions for automated testing and deployment
- **Monitoring**: Production model performance tracking
"""
        elif project_type == "nlp_rag_system":
            readme += """
### RAG (Retrieval Augmented Generation) System
- **Vector Store**: ChromaDB for efficient document retrieval
- **Embedding Pipeline**: Semantic search with state-of-the-art embeddings
- **LLM Generation**: Grounded responses using retrieved context
- **API**: FastAPI endpoints for document ingestion and querying
"""
        else:
            readme += """
### Core ML Pipeline
- **Data Processing**: Automated ETL and feature engineering
- **Model Training**: Configurable training pipeline
- **Deployment**: Containerized deployment with Docker/Kubernetes
"""
        
        readme += f"""

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
{"- NVIDIA GPU with CUDA 11.8+ (for GPU acceleration)" if "NVIDIA" in analysis["tech_stack"] else ""}
{"- Kubernetes cluster (for production deployment)" if "Kubernetes" in analysis["tech_stack"] else ""}

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd <project-directory>

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys (OPENAI_API_KEY, etc.)
```

### Running the Application

#### Development Mode
```bash
# Start the backend API
uvicorn src.api.main:app --reload --port 8000

# In a separate terminal, start the frontend (if applicable)
cd frontend
npm install
npm run dev
```

#### Production Mode (Docker)
```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build individual container
docker build -f deployments/docker/Dockerfile -t ai-platform:latest .
docker run -p 8000:8000 ai-platform:latest
```

{"#### Kubernetes Deployment" if "Kubernetes" in analysis["tech_stack"] else ""}
{"```bash" if "Kubernetes" in analysis["tech_stack"] else ""}
{"kubectl apply -f deployments/kubernetes/" if "Kubernetes" in analysis["tech_stack"] else ""}
{"```" if "Kubernetes" in analysis["tech_stack"] else ""}

## 📊 Tech Stack & Justification

| Technology | Purpose | Why Chosen |
|-----------|---------|------------|
"""
        
        tech_justifications = {
            "Python": "Core language | Industry standard for AI/ML with rich ecosystem",
            "PyTorch": "Deep Learning | Preferred for research and production flexibility",
            "TensorFlow": "Deep Learning | Google-backed, excellent for production deployment",
            "FastAPI": "API Framework | High performance, async support, automatic OpenAPI docs",
            "React": "Frontend | Component-based UI, large ecosystem",
            "Docker": "Containerization | Ensures consistency across environments",
            "Kubernetes": "Orchestration | Scalable, production-grade container orchestration",
            "OpenAI": "LLM Provider | State-of-the-art models (GPT-4, GPT-3.5)",
            "Anthropic": "LLM Provider | Claude for longer context and safety",
            "NVIDIA": "GPU Acceleration | CUDA for training acceleration, TensorRT for inference",
            "LangChain": "LLM Framework | Simplifies agent and chain development",
        }
        
        for tech in analysis["tech_stack"]:
            if tech in tech_justifications:
                readme += f"| {tech} | {tech_justifications[tech]} |\n"
        
        readme += f"""

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test suite
pytest tests/unit/ -v
pytest tests/integration/ -v
```

## 📈 Performance Considerations

- **Scalability**: Horizontal scaling via Kubernetes ReplicaSets
- **Caching**: Redis for API response caching
{"- **GPU Optimization**: CUDA kernels for training, TensorRT for inference" if "NVIDIA" in analysis["tech_stack"] else ""}
- **Async Processing**: FastAPI async endpoints for I/O-bound operations
- **Load Balancing**: NGINX ingress controller

## 🔒 Security & Compliance

- ✅ API key management via environment variables and Kubernetes secrets
- ✅ Input validation with Pydantic models
- ✅ Rate limiting on public endpoints
- ✅ HTTPS/TLS for all external communications
- ✅ Regular dependency updates and vulnerability scanning

## 📝 Industry Standards Compliance

This project follows industry best practices:

1. **Code Quality**: PEP 8 compliance, type hints, comprehensive docstrings
2. **Version Control**: Git with feature branching and semantic versioning
3. **CI/CD**: Automated testing and deployment pipelines
4. **Documentation**: Inline docs, architecture diagrams, API documentation
5. **Monitoring**: Logging, metrics, and alerting (Prometheus & Grafana ready)
{"6. **MLOps**: Experiment tracking (MLflow), model registry, A/B testing" if domain in ["mlops", "agentic_ai"] else ""}

## 🎓 Key Learnings & Design Decisions

### Why Multi-Agent Architecture?
{"Complex tasks benefit from decomposition. Each agent specializes in a specific capability, improving maintainability and performance." if project_type == "agentic_platform_enterprise" else ""}

### Why RAG over Fine-tuning?
{"RAG provides grounded responses without expensive fine-tuning. Ideal for dynamic knowledge bases." if project_type == "nlp_rag_system" else ""}

### Deployment Strategy
- **On-Premise**: Full control, data sovereignty (Kubernetes + NVIDIA GPUs)
- **Cloud**: Scalability, managed services (AWS Bedrock, GCP Vertex AI)
- **Hybrid**: Best of both worlds

## 📚 Additional Resources

- [API Documentation](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🤝 How This Aligns with Job Requirements

This project demonstrates:
"""
        
        if key_requirements:
            for req in key_requirements:
                readme += f"- ✅ **{req}**: Implemented and production-ready\n"
        
        readme += f"""
- ✅ **End-to-end AI Solutions**: From data ingestion to deployment
- ✅ **Scalable Architecture**: Kubernetes-ready with horizontal scaling
- ✅ **Best Practices**: Testing, CI/CD, monitoring, documentation
- ✅ **Modern Tech Stack**: {tech_stack_str}

---

**Built to showcase expertise in**: {domain.upper()} • {tech_stack_str} • Production Deployment
"""
        
        return readme
    
    def _generate_architecture(self, analysis, project_type, tech_stack_str, domain):
        """Generate detailed architecture documentation."""
        
        architecture = f"""# System Architecture

## Overview

This document describes the technical architecture of the {domain.upper()} solution.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend Layer                        │
│                  (React Dashboard - Optional)                │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTPS/REST
┌──────────────────────────▼──────────────────────────────────┐
│                       API Gateway                            │
│                    (FastAPI + NGINX)                         │
└──────────────────────────┬──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Agents     │  │   LLM Core   │  │   ML Engine  │
│              │  │              │  │              │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                  │
       └─────────────────┼──────────────────┘
                         │
                         ▼
              ┌──────────────────┐
              │   Data Layer     │
              │  (Vector Store,  │
              │   Model Registry)│
              └──────────────────┘
```

## Component Details

### 1. API Layer (`src/api/`)
- **Framework**: FastAPI with async support
- **Authentication**: API key + JWT tokens
- **Rate Limiting**: Token bucket algorithm
- **Endpoints**:
  - POST `/api/v1/execute` - Execute agent tasks
  - GET `/api/v1/agents` - List available agents
  - POST `/api/v1/upload` - Upload documents/data

"""
        
        if project_type == "agentic_platform_enterprise":
            architecture += """
### 2. Agent Layer (`src/agents/`)
- **Orchestrator**: Coordinates multiple specialized agents
- **Base Agent**: Abstract interface for all agents
- **Specialized Agents**:
  - Research Agent: Data gathering and analysis
  - Code Agent: Code generation and review
  - Planning Agent: Task decomposition
"""
        
        architecture += f"""

### 3. Core Services (`src/core/`)
- **LLM Client**: Abstracts multiple LLM providers (OpenAI, Anthropic, local)
- **Vector Store**: ChromaDB/Pinecone for semantic search
- **Model Registry**: MLflow for model versioning

### 4. Deployment (`deployments/`)
- **Docker**: Multi-stage builds for optimization
- **Kubernetes**: Deployment, Service, Ingress manifests
- **Secrets Management**: Kubernetes Secrets + External Secrets Operator

## Data Flow

1. **Request Reception**: API Gateway receives client request
2. **Authentication**: Validate API key/JWT
3. **Task Routing**: Route to appropriate service/agent
4. **Processing**: 
   - LLM calls for generation
   - Vector search for retrieval
   - Model inference for predictions
5. **Response**: JSON response with results

## Scalability Strategy

### Horizontal Scaling
- **API Pods**: Auto-scale based on CPU/memory
- **Worker Pods**: Scale based on queue depth
{"- **GPU Nodes**: NVIDIA device plugin for GPU scheduling" if "NVIDIA" in analysis["tech_stack"] else ""}

### Caching
- **Redis**: API response caching (5-minute TTL)
- **CDN**: Static assets via CloudFlare/CloudFront

## Security Architecture

1. **Network Layer**: Private VPC, security groups
2. **Application Layer**: Input validation, rate limiting
3. **Data Layer**: Encryption at rest (AES-256), in transit (TLS 1.3)
4. **Secrets**: Kubernetes Secrets + HashiCorp Vault

## Monitoring & Observability

- **Metrics**: Prometheus + Grafana
- **Logging**: ELK stack (Elasticsearch, Logstash, Kibana)
- **Tracing**: Jaeger for distributed tracing
- **Alerts**: PagerDuty integration

## Technology Stack Summary

{tech_stack_str}

## Future Enhancements

- [ ] A/B testing framework for model comparison
- [ ] Real-time streaming with WebSockets
- [ ] Multi-region deployment for low latency
- [ ] Advanced caching with Redis Cluster
"""
        
        return architecture
