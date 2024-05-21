from flask import Blueprint, jsonify, render_template, request

from professional_secure_ai_bot.chatbots.web_assistant_chatbot import (
    web_assistant_answer,
)

web_assistant_chatbot = Blueprint("web_assistant_chatbot_bp", __name__)


@web_assistant_chatbot.route("/ask", methods=["POST"])
def ask_question():
    """This route is used to send the question for answering."""
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Question is required."}), 400
    answer = web_assistant_answer(question)
    return jsonify({"answer": answer})


@web_assistant_chatbot.route("/chat")
def chat():
    """Renders the chat template with the right route and title."""
    return render_template(
        "base_chat.html",
        ajax_url="web_assistant_chatbot_bp.ask_question",
        chatbot_title="Web and files enabled assistant",
    )
