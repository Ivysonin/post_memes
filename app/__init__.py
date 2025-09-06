from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    from app.models import User, Meme, Comentario

    from app.controllers.comentario_controller import comentario_bp
    from app.controllers.meme_controller import meme_bp
    app.register_blueprint(comentario_bp)
    app.register_blueprint(meme_bp)

    return app