from flask import Blueprint, render_template, request

from professional_secure_ai_bot.chatbots.xss_chatbot import chat_with_bot

xss_demo_bp = Blueprint("xss_demo", __name__)


@xss_demo_bp.route("/xss", methods=["GET", "POST"])
def xss_demo():
    """On GET it renders the the template for the chat and on POST it embeds the answer directly into HTNL without filters."""
    if request.method == "GET":
        return render_template("xss_demo.html", chatbot_response=None)
    elif request.method == "POST":
        user_input = request.form["user_input"]
        response = chat_with_bot(user_input)

        # Intentionally vulnerable part: directly using the input and output without sanitization or encoding
        return render_template(
            "xss_demo.html", user_input=user_input, chatbot_response=response["text"]
        )
