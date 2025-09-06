from app.services.data_service import horario_local
from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=False)
    data_criacao = db.Column(db.DateTime, default=horario_local)

    memes = db.relationship("Meme", back_populates="author", cascade="all, delete-orphan")
    comentario = db.relationship("Comentario", back_populates="author", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<User {self.nome}>"