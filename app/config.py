from dotenv import load_dotenv
import os
load_dotenv('.env')


class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload de imagens
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "app", "static", "uploads")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB 
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}