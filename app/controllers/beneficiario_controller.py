from fastapi import APIRouter, HTTPException, status
from app.models.beneficiario import BeneficiarioCreate, BeneficiarioResponse
import re

router = APIRouter(prefix="/beneficiarios", tags=["Beneficiários"])

# Simulação de banco em memória para o MVP inicial (será substituído pela sessão PostgreSQL)
db_beneficiarios = [
    {
        "id": 1,
        "nome": "Maria das Dores Souza",
        "cpf": "12345678900",
        "membros_familia": 4,
        "elegivel_mes_atual": True,
        "status_texto": "Elegível - Cesta Liberada"
    }
]

@router.get("/{cpf}", response_model=BeneficiarioResponse)
def buscar_por_cpf(cpf: str):
    cpf_limpo = re.sub(r"\D", "", cpf)
    if len(cpf_limpo) != 11:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF incompleto. Digite os 11 dígitos numéricos."
        )
    
    for b in db_beneficiarios:
        if b["cpf"] == cpf_limpo:
            return b
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Beneficiário não encontrado na base da ACCTP."
    )

@router.post("/", response_model=BeneficiarioResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_beneficiario(dados: BeneficiarioCreate):
    for b in db_beneficiarios:
        if b["cpf"] == dados.cpf:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um cadastro ativo com este CPF."
            )
            
    novo_registro = {
        "id": len(db_beneficiarios) + 1,
        "nome": dados.nome,
        "cpf": dados.cpf,
        "membros_familia": dados.membros_familia,
        "elegivel_mes_atual": True,
        "status_texto": "Elegível - Cesta Liberada"
    }
    db_beneficiarios.append(novo_registro)
    return novo_registro