from flask import Blueprint, request, redirect, url_for, flash, render_template
from app.services.comentario_service import add_comentario
from app.models.meme_model import Meme


comentario_bp = Blueprint("comentario", __name__)


@comentario_bp.route("/meme/<int:meme_id>", methods=["GET"])
def meme_detail(meme_id):
    meme = Meme.query.get_or_404(meme_id)

    return render_template("meme_detalhes.html", meme=meme)


@comentario_bp.route("/meme/<int:meme_id>/comentario", methods=["POST"])
def post_comentario(meme_id):
    username = request.form.get("username")
    content = request.form.get("content")

    try:
        add_comentario(username, content, meme_id)
        flash("Comentário adicionado!", "success")
    except Exception as e:
        flash(str(e), "error")

    return redirect(url_for("comentario.meme_detail", meme_id=meme_id))