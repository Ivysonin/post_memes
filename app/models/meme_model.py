from app.services.data_service import horario_local
from datetime import datetime
from app import db


class Meme(db.Model):
    __tablename__ = "memes"

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, default=horario_local)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    author = db.relationship("User", back_populates="memes")
    comentario = db.relationship("Comentario", back_populates="meme", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Meme {self.id} do User {self.user_id}>"