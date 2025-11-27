import re
import os

class AgentEngine:
    def __init__(self):
        self.keywords = {
            "agentic_ai": ["agentic", "agent", "multi-agent", "orchestration", "autonomous", "mcp", "tool calling"],
            "genai": ["generative ai", "llm", "large language model", "gpt", "claude", "gemini", "llama", "openai", "anthropic"],
            "mlops": ["mlops", "llmops", "aiops", "ci/cd", "pipeline", "deployment", "kubernetes", "docker"],
            "cv": ["computer vision", "image", "cnn", "yolo", "detection", "segmentation", "vlm", "vision language"],
            "nlp": ["nlp", "natural language", "text", "transformer", "bert", "rag", "embeddings"],
            "enterprise": ["enterprise", "scalable", "production", "on-premise", "cloud", "nvidia", "gpu"]
        }

    def analyze(self, jd_text: str) -> dict:
        """Enhanced analysis with role detection and complexity scoring."""
        jd_lower = jd_text.lower()
        
        # Detect Seniority Level
        seniority = "mid"
        if any(keyword in jd_lower for keyword in ["senior", "sr.", "lead", "principal", "architect"]):
            seniority = "senior"
        elif any(keyword in jd_lower for keyword in ["junior", "entry", "associate"]):
            seniority = "junior"
        
        # Enhanced Tech Stack Detection
        tech_stack = []
        tech_map = {
            "Python": ["python"],
            "PyTorch": ["pytorch"],
            "TensorFlow": ["tensorflow"],
            "React": ["react", "react.js", "reactjs"],
            "FastAPI": ["fastapi"],
            "Docker": ["docker", "container"],
            "Kubernetes": ["kubernetes", "k8s"],
            "OpenAI": ["openai", "gpt-4", "gpt-3.5"],
            "Anthropic": ["anthropic", "claude"],
            "LangChain": ["langchain"],
            "NVIDIA": ["nvidia", "cuda", "tensorrt"],
            "Hugging Face": ["hugging face", "transformers"],
            "AWS": ["aws", "bedrock", "sagemaker"],
        }
        
        for tech, keywords in tech_map.items():
            if any(kw in jd_lower for kw in keywords):
                tech_stack.append(tech)
        
        if not tech_stack:
            tech_stack = ["Python", "Docker"]
        
        # Detect Domain with scoring
        domain_scores = {}
        for domain, keywords in self.keywords.items():
            score = sum(1 for kw in keywords if kw in jd_lower)
            if score > 0:
                domain_scores[domain] = score
        
        # Determine primary domain
        if not domain_scores:
            primary_domain = "basic_ml"
        else:
            primary_domain = max(domain_scores, key=domain_scores.get)
        
        # Extract Business Goal
        goal_patterns = [
            r"(to\s+(?:design|develop|build|create|implement|deploy)\s+[^.]{10,80})",
            r"(seeking.*?to\s+[^.]{10,80})",
        ]
        business_goal = "build advanced AI solutions"
        for pattern in goal_patterns:
            match = re.search(pattern, jd_lower)
            if match:
                business_goal = match.group(1).strip()
                break
        
        # Extract Key Requirements
        key_requirements = []
        if "mlops" in jd_lower or "llmops" in jd_lower:
            key_requirements.append("MLOps/LLMOps pipeline")
        if "kubernetes" in jd_lower or "k8s" in jd_lower:
            key_requirements.append("Kubernetes deployment")
        if "rag" in jd_lower:
            key_requirements.append("RAG implementation")
        if "agent" in jd_lower and "multi" in jd_lower:
            key_requirements.append("Multi-agent system")
        
        return {
            "tech_stack": tech_stack,
            "domain": primary_domain,
            "seniority": seniority,
            "business_goal": business_goal,
            "key_requirements": key_requirements,
            "domain_scores": domain_scores,
            "raw_text": jd_text
        }

    def architect(self, analysis: dict) -> str:
        """Select sophisticated project architecture based on analysis."""
        domain = analysis["domain"]
        seniority = analysis["seniority"]
        
        # For Agentic AI / GenAI roles
        if domain == "agentic_ai" or domain == "genai":
            if seniority == "senior":
                return "agentic_platform_enterprise"
            else:
                return "agentic_chatbot"
        
        # For MLOps focused roles
        elif domain == "mlops":
            return "mlops_pipeline"
        
        # For CV roles
        elif domain == "cv":
            if seniority == "senior":
                return "cv_multimodal"
            return "cv_classification"
        
        # For NLP roles
        elif domain == "nlp":
            if "RAG" in analysis.get("key_requirements", []):
                return "nlp_rag_system"
            return "nlp_transformer"
        
        else:
            return "ml_pipeline"
    
    def generate_project_scenario(self, analysis: dict, project_type: str) -> dict:
        """Generate a concrete, real-world project scenario with business context."""
        
        scenarios = {
            "agentic_platform_enterprise": {
                "title": "Enterprise Customer Support Automation Platform",
                "problem": "Customer support teams at mid-size SaaS companies handle 5,000+ tickets/month. 70% are repetitive questions about account management, billing, and basic troubleshooting, costing $300K/year in support staff time.",
                "solution": "Multi-agent AI system that handles tier-1 support automatically, escalating complex issues to humans.",
                "roi": "$210K annual savings (70% automation rate)",
                "dataset": "Sample support tickets dataset included",
                "use_case": "SaaS company with 10K users",
                "metrics": {
                    "resolution_rate": "85%",
                    "avg_response_time": "< 2 seconds",
                    "cost_per_ticket": "$0.05 (vs $3.00 human agent)"
                },
                "sample_data": self._generate_support_ticket_data()
            },
            "mlops_pipeline": {
                "title": "Fraud Detection System for E-Commerce",
                "problem": "E-commerce platform processes 50K transactions/day. Currently loses 1.8% of revenue ($2.7M annually) to fraudulent transactions while also blocking 9% of legitimate purchases (false positives).",
                "solution": "Real-time fraud scoring system using ensemble ML models with continuous retraining pipeline.",
                "roi": "$2.1M fraud loss prevention + $500K recovered from reduced false positives",
                "dataset": "Synthetic transaction data generator included",
                "use_case": "Mid-size e-commerce platform ($150M GMV)",
                "metrics": {
                    "fraud_detection_rate": "92%",
                    "false_positive_rate": "2.5%",
                    "latency": "< 50ms"
                },
                "sample_data": self._generate_transaction_data()
            },
            "nlp_rag_system": {
                "title": "Enterprise Knowledge Base Q&A System",
                "problem": "Company has 10K+ internal documentation pages. Employees spend 2 hours/week searching for information across Confluence, SharePoint, and Google Drive, costing $500K/year in lost productivity.",
                "solution": "RAG-powered search system that provides instant, cited answers from company knowledge base.",
                "roi": "$400K productivity savings annually",
                "dataset": "Sample company documentation included",
                "use_case": "500-person company with distributed knowledge",
                "metrics": {
                    "answer_accuracy": "88%",
                    "avg_search_time": "10 seconds (vs 15 minutes)",
                    "citation_accuracy": "95%"
                },
                "sample_data": self._generate_documentation_data()
            },
            "cv_classification": {
                "title": "Defect Detection for Manufacturing QA",
                "problem": "Manufacturing line produces 10K units/day. Manual inspection catches only 85% of defects, resulting in $500K/year in warranty claims and rework costs.",
                "solution": "Computer vision system for real-time defect detection with 98% accuracy.",
                "roi": "$425K savings from reduced defects and rework",
                "dataset": "Synthetic defect images generator included",
                "use_case": "Electronics manufacturing facility",
                "metrics": {
                    "defect_detection_rate": "98%",
                    "false_positive_rate": "3%",
                    "inspection_speed": "2 seconds/unit (vs 30 seconds human)"
                },
                "sample_data": self._generate_defect_data_script()
            },
            "cv_multimodal": {
                "title": "Medical Imaging Diagnosis Assistant",
                "problem": "Radiologists spend 15 minutes per chest X-ray scan. Hospital processes 200 scans/day. Small abnormalities (pneumonia, fractures) are missed in 5% of cases.",
                "solution": "AI-powered diagnostic assistant providing instant analysis with visual heatmaps.",
                "roi": "50% faster diagnosis + 80% reduction in missed findings",
                "dataset": "NIH Chest X-Ray dataset integration guide",
                "use_case": "Regional hospital with radiology department",
                "metrics": {
                    "diagnostic_accuracy": "94%",
                    "sensitivity": "96%",
                    "time_saved": "7.5 minutes/scan"
                },
                "sample_data": self._generate_medical_data_script()
            }
        }
        
        # Default to a generic scenario if not found
        default_scenario = {
            "title": "AI-Powered Data Analysis Platform",
            "problem": "Teams spend hours manually analyzing data and generating reports.",
            "solution": "Automated ML pipeline for data insights and predictions.",
            "roi": "60% time savings on analytical tasks",
            "dataset": "Sample CSV data included",
            "use_case": "Data-driven organization",
            "metrics": {"accuracy": "85%", "processing_time": "< 1 minute"},
            "sample_data": self._generate_generic_data()
        }
        
        return scenarios.get(project_type, default_scenario)
    
    def _generate_support_ticket_data(self):
        return {
            "type": "json",
            "filename": "data/sample_tickets.json",
            "content": '''[
    {
        "id": "T001",
        "category": "password_reset",
        "message": "I forgot my password and can't log in",
        "severity": "medium",
        "expected_agent": "account_management"
    },
    {
        "id": "T002",
        "category": "billing",
        "message": "Why was I charged twice this month?",
        "severity": "high",
        "expected_agent": "billing"
    },
    {
        "id": "T003",
        "category": "technical",
        "message": "The app crashes when I try to export data",
        "severity": "high",
        "expected_agent": "technical_support"
    }
]'''
        }
    
    def _generate_transaction_data(self):
        return {
            "type": "python",
            "filename": "data/generate_transactions.py",
            "content": '''import random
import json
from datetime import datetime, timedelta

def generate_sample_transactions(n=1000):
    """Generate synthetic transaction data for testing fraud detection."""
    transactions = []
    
    for i in range(n):
        # 2% fraudulent transactions
        is_fraud = random.random() < 0.02
        
        transaction = {
            "transaction_id": f"TXN{i:06d}",
            "amount": round(random.uniform(10, 5000) if not is_fraud else random.uniform(1000, 10000), 2),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
            "merchant_category": random.choice(["electronics", "clothing", "food", "travel"]),
            "device_id": f"DEV{random.randint(1, 100)}" if not is_fraud else f"DEV{random.randint(9000, 9999)}",
            "ip_country": "US" if not is_fraud else random.choice(["US", "NG", "RU", "CN"]),
            "is_fraud": is_fraud
        }
        transactions.append(transaction)
    
    return transactions

if __name__ == "__main__":
    data = generate_sample_transactions(1000)
    with open("sample_transactions.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {len(data)} transactions")
'''
        }
    
    def _generate_documentation_data(self):
        return {
            "type": "markdown",
            "filename": "data/sample_knowledge_base.md",
            "content": '''# Sample Company Knowledge Base

## Onboarding Guide

### How to Request Access
To request access to systems, submit a ticket to IT Help Desk with your manager's approval.

### VPN Setup
1. Download Cisco AnyConnect from the IT portal
2. Use your employee ID as username
3. Contact IT if you encounter "authentication failed"

## Engineering Practices

### Code Review Process
All PRs require 2 approvals before merging. Use the template in .github/PULL_REQUEST_TEMPLATE.md

### Deployment Schedule
Production deployments happen Tuesdays and Thursdays at 2 PM EST.

## Benefits

### PTO Policy
Employees accrue 15 days PTO per year. Submit requests via Workday at least 2 weeks in advance.
'''
        }
    
    def _generate_defect_data_script(self):
        return {
            "type": "python",
            "filename": "data/generate_defect_images.py",
            "content": '''"""
Synthetic defect image generator for testing.
In production, replace with real images from manufacturing line.
"""
import numpy as np
from PIL import Image, ImageDraw
import os

def generate_sample_images(output_dir="data/images", count=100):
    """Generate synthetic product images with random defects."""
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(f"{output_dir}/defective", exist_ok=True)
    os.makedirs(f"{output_dir}/normal", exist_ok=True)
    
    for i in range(count):
        # Create base image
        img = Image.new('RGB', (224, 224), color=(200, 200, 200))
        draw = ImageDraw.Draw(img)
        
        is_defective = i % 4 == 0  # 25% defective rate
        
        if is_defective:
            # Add a "scratch" defect
            draw.line([(50, 50), (170, 170)], fill=(100, 100, 100), width=3)
            img.save(f"{output_dir}/defective/img_{i:04d}.jpg")
        else:
            img.save(f"{output_dir}/normal/img_{i:04d}.jpg")
    
    print(f"Generated {count} sample images")

if __name__ == "__main__":
    generate_sample_images()
'''
        }
    
    def _generate_medical_data_script(self):
        return {
            "type": "markdown",
            "filename": "data/DATASET_INSTRUCTIONS.md",
            "content": '''# Medical Dataset Setup

## Using NIH Chest X-Ray Dataset

This project uses the publicly available NIH Chest X-Ray dataset.

### Download Instructions
1. Visit: https://www.kaggle.com/datasets/nih-chest-xrays/data
2. Download the dataset (42GB)
3. Extract to `data/chest_xrays/`

### Expected Structure
```
data/chest_xrays/
├── images/
│   ├── 00000001_000.png
│   ├── 00000001_001.png
│   └── ...
└── Data_Entry_2017.csv
```

### Sample Processing
See `src/preprocessing.py` for image loading and preprocessing pipeline.
'''
        }
    
    def _generate_generic_data(self):
        return {
            "type": "csv",
            "filename": "data/sample_data.csv",
            "content": '''id,feature1,feature2,feature3,target
1,0.5,1.2,3.4,0
2,1.1,2.3,4.5,1
3,0.8,1.9,3.1,0
4,1.5,2.8,5.2,1
5,0.6,1.4,3.7,0'''
        }

    def build(self, output_dir: str, project_type: str, analysis: dict):
        """Build sophisticated, role-aligned projects."""
        
        # Generate project scenario
        scenario = self.generate_project_scenario(analysis, project_type)
        
        # Create enhanced directory structure
        dirs = [
            "src/agents",
            "src/api",
            "src/core",
            "src/utils",
            "tests/unit",
            "tests/integration",
            "deployments/kubernetes",
            "deployments/docker",
            "mlops/pipelines",
            "data",
            "notebooks",
            "frontend/src",
            "docs"
        ]
        
        for dir_path in dirs:
            os.makedirs(os.path.join(output_dir, dir_path), exist_ok=True)
        
        # Generate PROJECT_SCENARIO.md
        self._create_scenario_doc(output_dir, scenario, analysis)
        
        # Generate sample data file
        self._create_sample_data(output_dir, scenario["sample_data"])
        
        # Generate based on project type
        if project_type == "agentic_platform_enterprise":
            self._create_agentic_platform(output_dir, analysis)
        elif project_type == "mlops_pipeline":
            self._create_mlops_pipeline(output_dir, analysis)
        elif project_type == "nlp_rag_system":
            self._create_rag_system(output_dir, analysis)
        else:
            # Fallback to enhanced basic template
            self._create_enhanced_basic(output_dir, analysis)
        
        # Always generate deployment configs
        self._create_deployment_configs(output_dir, analysis)
        self._create_requirements(output_dir, analysis)
        self._create_tests(output_dir, analysis)
    
    def _create_scenario_doc(self, output_dir, scenario, analysis):
        """Create PROJECT_SCENARIO.md explaining the concrete use case."""
        content = f"""# Project Scenario: {scenario['title']}

## 🎯 Real-World Problem

{scenario['problem']}

## 💡 Proposed Solution

{scenario['solution']}

## 💰 Business Value / ROI

{scenario['roi']}

## 📊 Use Case Context

**Target Customer**: {scenario['use_case']}
**Dataset**: {scenario['dataset']}

## 🎯 Target Metrics

"""
        for metric, value in scenario['metrics'].items():
            content += f"- **{metric.replace('_', ' ').title()}**: {value}\n"
        
        content += f"""

## 🔧 How to Use This Project

### 1. Run Sample Data Generation
```bash
# Generate or load sample data
python {scenario['sample_data']['filename']}
```

### 2. Train the Model
```bash
python src/train.py
```

### 3. Start the API
```bash
uvicorn src.api.main:app --reload
```

### 4. Test with Sample Queries
See `tests/integration/test_scenarios.py` for real-world test cases.

## 📈 Success Criteria

This project demonstrates:
- ✅ Solving a real ${scenario['roi'].split('$')[1].split(' ')[0] if '$' in scenario['roi'] else 'business'} problem
- ✅ Production-ready code with tests and deployment configs
- ✅ Clear business metrics and ROI
- ✅ Comprehensive documentation

## 🎓 Learning Outcomes

By implementing this project, you'll gain hands-on experience with:
- {analysis.get('domain', 'AI').upper()} applications in {scenario['use_case'].split()[0]} industry
- {', '.join(analysis.get('tech_stack', ['Python'])[:3])}
- Production ML deployment patterns
- Business-driven AI development

---

**This is not a toy example** - it simulates a real problem that{"".join([' ' + tech for tech in analysis.get('tech_stack', [])])} engineers solve daily.
"""
        
        with open(os.path.join(output_dir, "PROJECT_SCENARIO.md"), "w", encoding="utf-8") as f:
            f.write(content)
    
    def _create_sample_data(self, output_dir, sample_data_info):
        """Create the sample data file based on type."""
        filename = os.path.join(output_dir, sample_data_info['filename'])
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(sample_data_info['content'])

    def _create_agentic_platform(self, output_dir, analysis):
        """Create enterprise-grade Agentic AI platform."""
        
        # Multi-agent orchestrator
        with open(os.path.join(output_dir, "src/agents/orchestrator.py"), "w") as f:
            f.write('''"""
Multi-Agent Orchestration System
Coordinates multiple AI agents to solve complex, decomposed tasks.
"""
import asyncio
from typing import List, Dict, Any
from src.agents.base_agent import BaseAgent
from src.core.llm_client import LLMClient

class AgentOrchestrator:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.agents: List[BaseAgent] = []
        self.task_queue = asyncio.Queue()
    
    def register_agent(self, agent: BaseAgent):
        """Register an agent with the orchestrator."""
        self.agents.append(agent)
        print(f"Registered agent: {agent.name}")
    
    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Decompose and execute a complex task across multiple agents."""
        # Task decomposition using LLM
        subtasks = await self.llm_client.decompose_task(task)
        
        results = []
        for subtask in subtasks:
            # Route to appropriate agent
            agent = self._select_agent(subtask)
            result = await agent.execute(subtask)
            results.append(result)
        
        # Aggregate results
        final_result = await self.llm_client.aggregate_results(results)
        return final_result
    
    def _select_agent(self, subtask: Dict[str, Any]) -> BaseAgent:
        """Select the most appropriate agent for a subtask."""
        # Implementation for agent selection based on capabilities
        return self.agents[0]  # Simplified
''')
        
        # Base Agent
        with open(os.path.join(output_dir, "src/agents/base_agent.py"), "w") as f:
            f.write('''"""
Base Agent Interface
All agents must implement this interface.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    def __init__(self, name: str, capabilities: list):
        self.name = name
        self.capabilities = capabilities
    
    @abstractmethod
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a task and return the result."""
        pass
    
    @abstractmethod
    def can_handle(self, task: Dict[str, Any]) -> bool:
        """Determine if this agent can handle the given task."""
        pass
''')
        
        # LLM Client with multiple providers
        with open(os.path.join(output_dir, "src/core/llm_client.py"), "w") as f:
            f.write('''"""
LLM Client with support for multiple providers (OpenAI, Anthropic, Local models)
"""
import os
from typing import Optional, List, Dict, Any
import httpx

class LLMClient:
    def __init__(self, provider: str = "openai", model: str = "gpt-4"):
        self.provider = provider
        self.model = model
        self.api_key = os.getenv(f"{provider.upper()}_API_KEY")
    
    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate text using the configured LLM."""
        if self.provider == "openai":
            return await self._call_openai(prompt, **kwargs)
        elif self.provider == "anthropic":
            return await self._call_anthropic(prompt, **kwargs)
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")
    
    async def _call_openai(self, prompt: str, **kwargs) -> str:
        # Implementation for OpenAI API
        pass
    
    async def _call_anthropic(self, prompt: str, **kwargs) -> str:
        # Implementation for Anthropic API
        pass
    
    async def decompose_task(self, task: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Use LLM to decompose a complex task into subtasks."""
        prompt = f"Decompose this task into subtasks: {task}"
        response = await self.generate(prompt)
        # Parse response into subtasks
        return []  # Placeholder
    
    async def aggregate_results(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Use LLM to aggregate results from multiple agents."""
        prompt = f"Aggregate these results: {results}"
        response = await self.generate(prompt)
        return {"aggregated": response}
''')
        
        # FastAPI application
        with open(os.path.join(output_dir, "src/api/main.py"), "w") as f:
            f.write('''"""
FastAPI Application for Agentic AI Platform
Provides REST API for agent orchestration.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agents.orchestrator import AgentOrchestrator
from src.core.llm_client import LLMClient

app = FastAPI(title="Agentic AI Platform")

# Initialize orchestrator
llm_client = LLMClient(provider="openai", model="gpt-4")
orchestrator = AgentOrchestrator(llm_client)

class TaskRequest(BaseModel):
    description: str
    context: dict = {}

@app.post("/api/v1/execute")
async def execute_task(request: TaskRequest):
    """Execute a task using the multi-agent system."""
    try:
        result = await orchestrator.execute_task({
            "description": request.description,
            "context": request.context
        })
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/agents")
async def list_agents():
    """List all registered agents."""
    return {
        "agents": [
            {"name": agent.name, "capabilities": agent.capabilities}
            for agent in orchestrator.agents
        ]
    }
''')
        
        # React Frontend Component
        with open(os.path.join(output_dir, "frontend/src/AgentDashboard.jsx"), "w") as f:
            f.write('''import React, { useState } from 'react';
import axios from 'axios';

export default function AgentDashboard() {
    const [task, setTask] = useState('');
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const executeTask = async () => {
        setLoading(true);
        try {
            const response = await axios.post('/api/v1/execute', {
                description: task,
                context: {}
            });
            setResult(response.data.result);
        } catch (error) {
            console.error('Error executing task:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="agent-dashboard">
            <h1>Agentic AI Platform</h1>
            <textarea
                value={task}
                onChange={(e) => setTask(e.target.value)}
                placeholder="Enter task description..."
                rows={5}
            />
            <button onClick={executeTask} disabled={loading}>
                {loading ? 'Executing...' : 'Execute Task'}
            </button>
            {result && (
                <div className="result">
                    <h3>Result:</h3>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}
''')

    def _create_deployment_configs(self, output_dir, analysis):
        """Create Kubernetes and Docker deployment configs."""
        
        # Kubernetes Deployment
        with open(os.path.join(output_dir, "deployments/kubernetes/deployment.yaml"), "w") as f:
            f.write('''apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-platform
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-platform
  template:
    metadata:
      labels:
        app: ai-platform
    spec:
      containers:
      - name: app
        image: ai-platform:latest
        ports:
        - containerPort: 8000
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: ai-secrets
              key: openai-key
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
            nvidia.com/gpu: "1"
          limits:
            memory: "4Gi"
            cpu: "2000m"
            nvidia.com/gpu: "1"
''')
        
        # Dockerfile with NVIDIA support
        with open(os.path.join(output_dir, "deployments/docker/Dockerfile"), "w") as f:
            nvidia_base = "nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04" if "NVIDIA" in analysis["tech_stack"] else "python:3.10-slim"
            f.write(f'''FROM {nvidia_base}

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    build-essential \\
    git \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
''')

    def _create_mlops_pipeline(self, output_dir, analysis):
        """Create MLOps/LLMOps CI/CD pipeline."""
        
        with open(os.path.join(output_dir, "mlops/pipelines/training_pipeline.py"), "w") as f:
            f.write('''"""
MLOps Training Pipeline with experiment tracking and model registry.
"""
import mlflow
from typing import Dict, Any

class TrainingPipeline:
    def __init__(self, experiment_name: str):
        self.experiment_name = experiment_name
        mlflow.set_experiment(experiment_name)
    
    def run(self, config: Dict[str, Any]):
        """Execute the full training pipeline."""
        with mlflow.start_run():
            # Log parameters
            mlflow.log_params(config)
            
            # Data preprocessing
            data = self.load_and_preprocess_data(config["data_path"])
            
            # Model training
            model = self.train_model(data, config)
            
            # Evaluation
            metrics = self.evaluate_model(model, data)
            mlflow.log_metrics(metrics)
            
            # Model registration
            if metrics["accuracy"] > config["min_accuracy"]:
                mlflow.sklearn.log_model(model, "model")
                print("Model registered successfully!")
    
    def load_and_preprocess_data(self, data_path: str):
        # Implementation
        pass
    
    def train_model(self, data, config):
        # Implementation
        pass
    
    def evaluate_model(self, model, data):
        # Implementation
        return {"accuracy": 0.95}
''')
        
        # GitHub Actions workflow
        os.makedirs(os.path.join(output_dir, ".github/workflows"), exist_ok=True)
        with open(os.path.join(output_dir, ".github/workflows/mlops.yml"), "w") as f:
            f.write('''name: MLOps Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest
    - name: Run tests
      run: pytest tests/

  train:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run training pipeline
      run: python mlops/pipelines/training_pipeline.py
''')

    def _create_rag_system(self, output_dir, analysis):
        """Create RAG (Retrieval Augmented Generation) system."""
        
        with open(os.path.join(output_dir, "src/core/rag_engine.py"), "w") as f:
            f.write('''"""
RAG (Retrieval Augmented Generation) Engine
Combines vector search with LLM generation for accurate, grounded responses.
"""
from typing import List, Dict
import chromadb

class RAGEngine:
    def __init__(self, llm_client, collection_name: str = "knowledge_base"):
        self.llm_client = llm_client
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(collection_name)
    
    def add_documents(self, documents: List[Dict[str, str]]):
        """Add documents to the vector store."""
        self.collection.add(
            documents=[doc["text"] for doc in documents],
            ids=[doc["id"] for doc in documents],
            metadatas=[doc.get("metadata", {}) for doc in documents]
        )
    
    async def query(self, question: str, top_k: int = 5) -> str:
        """Query the RAG system."""
        # Retrieve relevant documents
        results = self.collection.query(
            query_texts=[question],
            n_results=top_k
        )
        
        # Build context from retrieved documents
        context = "\\n\\n".join(results["documents"][0])
        
        # Generate response using LLM
        prompt = f"""Based on the following context, answer the question.

Context:
{context}

Question: {question}

Answer:"""
        
        response = await self.llm_client.generate(prompt)
        return response
''')

    def _create_requirements(self, output_dir, analysis):
        """Generate comprehensive requirements.txt based on analysis."""
        
        requirements = [
            "# Core Dependencies",
            "fastapi==0.104.1",
            "uvicorn[standard]==0.24.0",
            "pydantic==2.5.0",
            "python-dotenv==1.0.0",
            "",
            "# ML/AI Libraries",
            "numpy==1.24.3",
            "pandas==2.0.3",
        ]
        
        if "PyTorch" in analysis["tech_stack"]:
            requirements.extend([
                "torch==2.1.0",
                "torchvision==0.16.0",
            ])
        
        if "NVIDIA" in analysis["tech_stack"]:
            requirements.append("nvidia-ml-py==12.535.77")
        
        if analysis["domain"] in ["agentic_ai", "genai"]:
            requirements.extend([
                "",
                "# LLM & Agent Libraries",
                "openai==1.3.0",
                "anthropic==0.7.0",
                "langchain==0.0.340",
                "chromadb==0.4.18",
            ])
        
        if "Kubernetes" in analysis["tech_stack"]:
            requirements.append("kubernetes==28.1.0")
        
        if analysis["domain"] == "mlops":
            requirements.extend([
                "",
                "# MLOps",
                "mlflow==2.8.1",
                "dvc==3.30.1",
            ])
        
        requirements.extend([
            "",
            "# Testing",
            "pytest==7.4.3",
            "pytest-asyncio==0.21.1",
            "httpx==0.25.1",
        ])
        
        with open(os.path.join(output_dir, "requirements.txt"), "w") as f:
            f.write("\n".join(requirements))

    def _create_tests(self, output_dir, analysis):
        """Generate comprehensive test suite."""
        
        with open(os.path.join(output_dir, "tests/test_api.py"), "w") as f:
            f.write('''"""
API Integration Tests
"""
import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check():
    """Test API health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_task_execution():
    """Test task execution endpoint."""
    response = client.post("/api/v1/execute", json={
        "description": "Test task",
        "context": {}
    })
    assert response.status_code == 200
    assert "result" in response.json()
''')

    def _create_enhanced_basic(self, output_dir, analysis):
        """Enhanced basic template as fallback."""
        self._create_requirements(output_dir, analysis)
        self._create_tests(output_dir, analysis)
        
        with open(os.path.join(output_dir, "src/main.py"), "w") as f:
            f.write(f'''"""
Main application for {analysis["business_goal"]}
"""
print("Application initialized for: {analysis['business_goal']}")
print("Tech Stack: {', '.join(analysis['tech_stack'])}")
''')
