from app.models.comentario_model import Comentario
from app.models.user_model import User
from app.models.meme_model import Meme
from app import db


def add_comentario(username, content, meme_id):
    """
    Adiciona um comentário a um meme específico no sistema.
    """

    if not content.strip():
        raise ValueError("Comentário vazio não é permitido.")

    # Garantir user
    user = User.query.filter_by(nome=username).first()
    if not user:
        user = User(nome=username)
        db.session.add(user)
        db.session.commit()

    meme = Meme.query.get(meme_id)
    if not meme:
        raise ValueError("Meme não encontrado.")

    comentario = Comentario(conteudo=content, author=user, meme=meme)
    db.session.add(comentario)
    db.session.commit()

    return comentario