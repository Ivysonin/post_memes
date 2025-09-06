from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.meme_service import save_meme
from app.models.meme_model import Meme


meme_bp = Blueprint("meme", __name__)


@meme_bp.route("/", methods=["GET"])
def index():
    memes = Meme.query.order_by(Meme.data_criacao.desc()).all()

    return render_template("index.html", memes=memes)


@meme_bp.route("/upload", methods=["POST"])
def upload_meme():
    username = request.form.get("username")
    file = request.files.get("file")

    try:
        save_meme(file, username)
        flash("Meme enviado com sucesso!", "success")
    except Exception as e:
        flash(str(e), "error")

    return redirect(url_for("meme.index"))