from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.hashing import hash_password, verify_password
from app.core.security import create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, name: str, email: str, password: str) -> User:
        user = self.db.query(User).filter(User.email == email).first()
        if user:
            raise ValueError("User already exists")
        new = User(name=name, email=email, hashed_password=hash_password(password))
        self.db.add(new)
        self.db.commit()
        self.db.refresh(new)
        return new

    def authenticate(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            return None
        token = create_access_token({"sub": str(user.id), "email": user.email})
        return token
