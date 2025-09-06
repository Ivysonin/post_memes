from app import db
from datetime import datetime
from app.services.data_service import horario_local


class Comentario(db.Model):
    __tablename__ = "comentario"

    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=horario_local)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    meme_id = db.Column(db.Integer, db.ForeignKey("memes.id"), nullable=False)

    author = db.relationship("User", back_populates="comentario")
    meme = db.relationship("Meme", back_populates="comentario")


    def __repr__(self):
        return f"<Comentario {self.id} do Meme {self.meme_id}>"