import os

from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.utils import safe_join

texteditor_bp = Blueprint("texteditor", __name__, template_folder="templates")

FILE_DIR = "./textfiles"


@texteditor_bp.route("/browse", methods=["GET", "POST"], defaults={"filename": None})
@texteditor_bp.route("/edit/<filename>", methods=["GET"])
def editor(filename):
    mode = "browse"
    files = None
    content = ""

    if request.method == "POST":
        new_filename = request.form.get("new_filename")
        if new_filename:
            new_filepath = safe_join(FILE_DIR, new_filename)
            if not os.path.exists(new_filepath):
                open(new_filepath, "w").close()
                return redirect(url_for(".editor", filename=new_filename))

    if filename:
        mode = "edit"
        filepath = safe_join(FILE_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
        except IOError:
            return redirect(url_for(".editor"))
    else:
        try:
            files = os.listdir(FILE_DIR)
            files = [f for f in files if os.path.isfile(os.path.join(FILE_DIR, f))]
        except Exception:
            files = []

    return render_template(
        "editor.html", mode=mode, files=files, filename=filename, content=content
    )


@texteditor_bp.route("/save/<filename>", methods=["POST"])
def save(filename):
    content = request.form["content"]
    filepath = safe_join(FILE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)
    return redirect(url_for(".editor", filename=filename))
