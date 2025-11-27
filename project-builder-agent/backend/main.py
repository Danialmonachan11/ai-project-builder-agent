from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from agent_engine import AgentEngine
from doc_generator import DocGenerator
import os
import shutil
import uuid
import re

app = FastAPI()

class JobDescription(BaseModel):
    text: str

def generate_project_name(analysis: dict, project_type: str) -> str:
    """Generate a meaningful project name based on analysis."""
    # Extract key components
    domain = analysis.get("domain", "ai")
    seniority = analysis.get("seniority", "mid")
    
    # Map project types to readable names
    type_names = {
        "agentic_platform_enterprise": "agentic_ai_platform",
        "agentic_chatbot": "ai_chatbot",
        "mlops_pipeline": "mlops_pipeline",
        "cv_classification": "cv_classifier",
        "cv_multimodal": "multimodal_cv",
        "nlp_transformer": "nlp_transformer",
        "nlp_rag_system": "rag_system",
        "ml_pipeline": "ml_pipeline"
    }
    
    base_name = type_names.get(project_type, domain + "_project")
    
    # Add seniority prefix for senior roles
    if seniority == "senior":
        base_name = "enterprise_" + base_name
    
    # Generate a short unique ID (6 characters)
    unique_id = str(uuid.uuid4())[:6]
    
    # Clean and format the name
    project_name = f"{base_name}_{unique_id}"
    
    # Ensure it's filesystem-safe
    project_name = re.sub(r'[^a-z0-9_]', '_', project_name.lower())
    
    return project_name

@app.post("/generate_project")
async def generate_project(jd: JobDescription):
    try:
        # 1. Analyze JD
        engine = AgentEngine()
        analysis = engine.analyze(jd.text)
        
        # 2. Select Architecture
        project_type = engine.architect(analysis)
        
        # 3. Generate meaningful project name
        project_name = generate_project_name(analysis, project_type)
        
        # 4. Generate Documentation
        doc_gen = DocGenerator()
        docs = doc_gen.generate(analysis, project_type)
        
        # 5. Build Project
        output_dir = f"temp_projects/{project_name}"
        os.makedirs(output_dir, exist_ok=True)
        
        # Build project structure
        engine.build(output_dir, project_type, analysis)
        
        # Get scenario info for frontend display
        scenario = engine.generate_project_scenario(analysis, project_type)
        
        # Write docs
        with open(f"{output_dir}/README.md", "w", encoding="utf-8") as f:
            f.write(docs["README.md"])
            
        with open(f"{output_dir}/ARCHITECTURE.md", "w", encoding="utf-8") as f:
            f.write(docs["ARCHITECTURE.md"])
            
        return {
            "status": "success",
            "analysis": analysis,
            "project_type": project_type,
            "project_id": project_name,
            "project_name": project_name,  # User-friendly name
            "scenario": {
                "title": scenario["title"],
                "problem": scenario["problem"],
                "solution": scenario["solution"],
                "roi": scenario["roi"]
            },
            "files": ["README.md", "ARCHITECTURE.md", "PROJECT_SCENARIO.md"]
        }

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error generating project: {error_details}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/download/{project_id}")
async def download_project(project_id: str):
    project_path = f"temp_projects/{project_id}"
    if not os.path.exists(project_path):
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Create zip with the project name
    zip_path = f"temp_projects/{project_id}"
    shutil.make_archive(zip_path, 'zip', project_path)
    
    # Return the file with proper headers for download
    return FileResponse(
        f"{zip_path}.zip", 
        filename=f"{project_id}.zip", 
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename={project_id}.zip"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
