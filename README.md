# API de Autenticação - FastAPI + JWT

Projeto simples de **API de autenticação** feito com **FastAPI**.  
Permite registrar usuários, fazer login e acessar rotas protegidas usando **JWT**.  

Feito como projeto de estudo / portfólio de engenharia de software júnior.

---

## Tecnologias usadas

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT (PyJWT)
- Passlib (bcrypt)
- Docker / Docker Compose

---

## Funcionalidades

- Registrar novo usuário (`POST /auth/register`)
- Login com e-mail e senha (`POST /auth/login`)
- Acesso a rota protegida (`GET /users/me`)

---

## Como rodar

1. Clonar repositório:
```bash
git clone https://github.com/Dariodev7/api-auth-system-frontend.git
cd api-auth-system-frontend
Criar arquivo .env baseado em .env.example.

Rodar com Docker:

bash
Copiar código
docker-compose up --build
A aplicação ficará disponível em: http://127.0.0.1:8000

Testando rapidamente (PowerShell)
Registrar usuário:

powershell
Copiar código
Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:8000/auth/register" `
-Body (@{ name="Teste"; email="teste@teste.com"; password="123456" } | ConvertTo-Json) `
-ContentType "application/json"
Fazer login:

powershell
Copiar código
Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:8000/auth/login" `
-Body (@{ email="teste@teste.com"; password="123456" } | ConvertTo-Json) `
-ContentType "application/json"
Documentação
Acesse a documentação interativa do FastAPI:
http://127.0.0.1:8000/docs
