from fastapi import FastAPI
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