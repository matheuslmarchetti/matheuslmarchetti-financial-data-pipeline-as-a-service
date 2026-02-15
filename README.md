# 🚀 Financial Data Pipeline as a Service

Pipeline de dados financeiros automatizado com coleta diária, validação, versionamento e disponibilização via API REST segura e versionada.

---

## 📌 Objetivo

Evoluir o projeto anterior **Market Insight Automation API** para uma arquitetura profissional de Engenharia de Dados, simulando um ambiente real de empresa.

Este projeto implementa:

- Coleta automatizada de dados financeiros
- Validação e tratamento de dados
- Versionamento de dados
- Armazenamento estruturado em PostgreSQL
- API REST versionada
- Autenticação com JWT
- Controle de acesso por roles
- Logs estruturados
- Observabilidade com métricas
- Simulação de ambientes (dev / staging / prod)
- Pipeline com reprocessamento

---

## 🏗 Arquitetura

O projeto é dividido em duas grandes camadas:

### 1️⃣ Data Pipeline
Responsável por:
- Coleta de dados de mercado (yFinance)
- Dados macroeconômicos (FRED)
- Notícias (Google News RSS via feedparser)
- Validação
- Persistência
- Registro de execução do pipeline

### 2️⃣ API REST
Responsável por:
- Expor dados versionados
- Autenticação via OAuth2 + JWT
- Controle de acesso
- Rate limit
- Logs estruturados
- Health checks
- Métricas

---

## 🛠 Tecnologias Utilizadas

- Python 3.13
- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Alembic
- APScheduler
- yFinance
- fredapi
- feedparser
- Docker & Docker Compose
- Prometheus (métricas)
- GitHub Actions (CI/CD)

---

## 🔐 Segurança

- OAuth2 Password Flow
- JWT
- Controle de acesso por roles
- Rate limiting
- Versionamento de API (/api/v1)

---

## 📊 Observabilidade

- Logs estruturados em JSON
- Métricas de performance
- Monitoramento de execução do pipeline
- Endpoints de health check

---

## 📁 Estrutura do Projeto

```

financial-data-pipeline-as-a-service/
│
├── app/
├── tests/
├── docker-compose.yml
├── Dockerfile
├── .env.dev
├── .env.staging
├── .env.prod
└── README.md

```

---

## 🎯 Objetivo Profissional

Este projeto foi desenvolvido com foco em preparação para vagas como:

- Engenheiro de Dados Jr
- Engenheiro de Machine Learning Jr
- Analista Desenvolvedor de Sistemas (APIs)
- Backend Engineer

---

## 🚀 Próximos Passos

- Implementação do pipeline automatizado
- Versionamento de dados
- Autenticação e autorização
- Observabilidade
- CI/CD

---

## 📚 Contexto

Este projeto é a evolução do:

**Market Insight Automation API**

Agora estruturado como um pipeline de dados profissional com arquitetura escalável.

---

## 👨‍💻 Autor

Matheus Marchetti
