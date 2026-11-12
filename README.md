# ACCTP — Logística Socioassistencial (MVP PWA)

> Sistema de triagem, controle de entregas e gestão de estoque para otimização do atendimento comunitário da ACCTP, desenvolvido com foco em acessibilidade e eficiência operacional. Alinhado à **Meta 2.1 do ODS 2 (Fome Zero e Agricultura Sustentável)**.

---

## Sobre o Projeto

O **ACCTP MVP** é um Progressive Web App (PWA) integrado a uma API em Python/FastAPI, projetado para resolver gargalos críticos em centros de distribuição socioassistencial (como filas prolongadas e riscos de entregas duplicadas). O sistema substitui fichas de papel por um fluxo digital ágil, seguro e acessível.

### Funcionalidades Principais (Fluxo de 3 Telas)
1. **Tela 1 (Dashboard e Busca):** Pesquisa instantânea de assistidos por CPF com máscara automática, validação estricta e botões de acesso rápido otimizados para toque.
2. **Tela 2 (Prontuário e Baixa Transacional):** Exibição de elegibilidade com **Banner Multisensorial (Cor + Símbolo + Texto)**, impedindo entregas duplicadas no mesmo ciclo mensal e registrando a baixa atômica no estoque.
3. **Tela 3 (Painel de Estoque e Validade):** Monitoramento de lotes perecíveis ordenados por prioridade, utilizando tags geométricas (octógono e triângulo) para identificação rápida de vencimento iminente (48h e 5 dias).

---

##  Stack Tecnológica

* **Backend / API:** Python 3.12, FastAPI, Pydantic, SQLAlchemy.
* **Banco de Dados:** PostgreSQL (compatível com Supabase / Render).
* **Interface / PWA:** HTML5, Tailwind CSS, JavaScript (Service Workers para suporte offline parcial).
* **Testes e Qualidade:** Pytest, HTTPX, Git & GitHub Actions (CI/CD).

---

##  Estrutura de Diretórios

```text
acctp-mvp-logistica/
├── app/
│   ├── __init__.py
│   ├── main.py                    # Ponto de entrada FastAPI e health check
│   ├── controllers/               # Rotas e endpoints da API
│   ├── models/                    # Modelos de dados e validações Pydantic
│   ├── services/                  # Regras de negócio e transações
│   └── views/                     # Interface PWA (HTML/CSS/JS)
├── tests/
│   └── test_beneficiario.py       # Testes unitários com pytest
├── requirements.txt               # Dependências do projeto
├── .env.example                   # Exemplo de variáveis de ambiente
└── README.md                      # Documentação do projeto