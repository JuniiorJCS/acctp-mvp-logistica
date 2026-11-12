from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from app.controllers.beneficiario_controller import router as beneficiario_router

app = FastAPI(
    title="ACCTP - API Logística Socioassistencial",
    description="MVP para gestão de estoque e triagem de assistidos (ODS 2)",
    version="0.1.0"
)

app.include_router(beneficiario_router)

@app.get("/health")
def health_check():
    return {"status": "online", "projeto": "ACCTP MVP"}

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    html_file = Path("app/templates/index.html")
    return html_file.read_text(encoding="utf-8")