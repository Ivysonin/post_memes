from werkzeug.utils import secure_filename
from app.models.meme_model import Meme
from app.models.user_model import User
from flask import current_app
from app import db
import os


def allowed_file(filename):
    """
    Verifica se um arquivo tem uma extensão permitida para upload.
    """

    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]


def save_meme(file, username):
    """
    É responsável por salvar uma imagem de meme enviada por um usuário
    e registrar essa informação no banco de dados.
    """
    
    if not file or file.filename == "":
        raise ValueError("Nenhum arquivo enviado.")

    if not allowed_file(file.filename):
        raise ValueError("Formato de arquivo não permitido.")

    # Garantir user
    user = User.query.filter_by(nome=username).first()
    if not user:
        user = User(nome=username)
        db.session.add(user)
        db.session.commit()

    # Salvar arquivo
    filename = secure_filename(file.filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)

    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)

    # Criar meme no banco (salva apenas caminho relativo dentro de /static)
    meme = Meme(image_url=f"uploads/{filename}", author=user)
    db.session.add(meme)
    db.session.commit()

    return meme