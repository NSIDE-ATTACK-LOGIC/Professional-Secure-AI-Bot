from flask import Blueprint, render_template, request

from professional_secure_ai_bot.data_tools.chhroma_handler import (
    add_to_chroma,
    do_similarity_search,
)

text_management_bp = Blueprint("text_management", __name__, template_folder="templates")


# If POST, it will add to DB
# If GET it will do similarity search
@text_management_bp.route("/submit-text", methods=["GET", "POST"])
def submit_text():
    documents = []
    if request.method == "POST":
        if "text" in request.form:
            text = request.form["text"]
            add_to_chroma(text)

        if "newText" in request.form:
            new_text = request.form["newText"]
            documents = do_similarity_search(new_text)

    return render_template("submit_text.html", documents=documents)
