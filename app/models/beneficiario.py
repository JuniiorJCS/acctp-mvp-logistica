from pydantic import BaseModel, Field, field_validator
import re

class BeneficiarioCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=120, description="Nome completo do responsável")
    cpf: str = Field(..., description="CPF com ou sem pontuação")
    membros_familia: int = Field(..., ge=1, le=20, description="Quantidade de integrantes na família")

    @field_validator("cpf")
    @classmethod
    def validar_cpf(cls, valor: str) -> str:
        # Remove pontos e traços, mantendo apenas números
        apenas_digitos = re.sub(r"\D", "", valor)
        if len(apenas_digitos) != 11:
            raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")
        return apenas_digitos

class BeneficiarioResponse(BeneficiarioCreate):
    id: int
    elegivel_mes_atual: bool = True
    status_texto: str = "Elegível - Cesta Liberada"