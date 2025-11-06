# src/main.py
from fastapi import FastAPI
from app.routes import auth

# import do DB para criar tabelas em dev
from app.db.database import Base, engine
import app.models.user  # importa os models para garantir o metadata

app = FastAPI(title="Dário.dev API")

# Health check (adicionar este endpoint)
@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

# Garantir criação das tabelas (apenas para desenvolvimento)
Base.metadata.create_all(bind=engine)

@app.get("/", tags=["root"])
def root():
    return {"message": "Servidor Dário.dev API funcionando!"}

# Incluir routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
