# Financial Data Pipeline as a Service

## 📌 Visão Geral

Plataforma profissional de dados financeiros desenvolvida com FastAPI e PostgreSQL.

O sistema realiza ingestão automatizada de dados de mercado (yFinance, FRED e RSS), controla execuções de pipeline, versiona datasets e fornece API segura com autenticação JWT.

Projetado como base confiável para sistemas de Inteligência Artificial.

---

## 🎯 Objetivo do Projeto

Construir uma infraestrutura de dados financeiros que:

* Realiza ingestão automatizada de múltiplas fontes
* Rastreia execuções de pipeline
* Versiona datasets para reprodutibilidade
* Garante segurança com autenticação JWT
* Possui observabilidade e logs estruturados
* Está pronta para deploy em ambiente profissional

Este projeto serve como camada de dados para futuros sistemas de IA e ML.

---

## 🏗 Arquitetura

Arquitetura em camadas:

* API (FastAPI)
* Service Layer (regras de negócio)
* Repository Layer (acesso a dados)
* PostgreSQL
* Autenticação JWT
* Sistema de rastreamento de pipeline

---

## 🔐 Segurança

* Autenticação JWT
* Controle de acesso por roles (admin / user)
* Hash seguro de senha
* Configuração por variáveis de ambiente

---

## 📊 Conceitos de Engenharia de Dados Aplicados

* Versionamento de dados
* Rastreabilidade de ingestão
* Metadata de execução
* Reprocessamento controlado
* Estrutura orientada a ML
* Logs estruturados

---

## 🌎 Fontes de Dados

* yFinance (ativos financeiros)
* FRED (indicadores macroeconômicos)
* RSS financeiro (notícias)

---

## 🚀 Tecnologias

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT
* Docker
* Render

---

## 🧠 Integração Futura com IA

A plataforma foi projetada para servir como base de dados para:

* Sistemas de análise de sentimento
* Modelos de previsão financeira
* Sistemas de recomendação
* Relatórios inteligentes automatizados

---

## 👨‍💻 Autor

**Matheus Lunguinho Marchetti**
Python | Dados | Automação | APIs | IA
