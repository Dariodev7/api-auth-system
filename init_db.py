from app.db.database import engine
from app.db.base import Base
import app.models.user  # garante que o modelo User é registrado

print(">> Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print(">> Tabelas criadas com sucesso ✅")
