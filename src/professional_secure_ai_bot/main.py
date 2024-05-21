from flask import Flask, render_template

from professional_secure_ai_bot.blueprints.rag_chatbot_bp import rag_chatbot
from professional_secure_ai_bot.blueprints.text_management_bp import text_management_bp
from professional_secure_ai_bot.blueprints.texteditor_bp import texteditor_bp
from professional_secure_ai_bot.blueprints.user_manage_chatbot_bp import (
    user_manage_chatbot,
)
from professional_secure_ai_bot.blueprints.web_assistant_bp import web_assistant_chatbot
from professional_secure_ai_bot.blueprints.xss_demo_bp import xss_demo_bp
from professional_secure_ai_bot.data_tools.chhroma_handler import init_chroma_db

app = Flask(__name__)

app.register_blueprint(xss_demo_bp)
app.register_blueprint(text_management_bp, url_prefix="/text-management")
app.register_blueprint(rag_chatbot, url_prefix="/rag-chatbot")
app.register_blueprint(user_manage_chatbot, url_prefix="/user_manage_chatbot")
app.register_blueprint(texteditor_bp, url_prefix="/text-editor")
app.register_blueprint(web_assistant_chatbot, url_prefix="/web-assistant")


@app.route("/")
def home():
    """Renders the main website."""
    return render_template("index.html")


def main():
    init_chroma_db()
    app.run(
        debug=True,
        use_reloader=False,
        host="0.0.0.0",
    )


if __name__ == "__main__":
    main()
