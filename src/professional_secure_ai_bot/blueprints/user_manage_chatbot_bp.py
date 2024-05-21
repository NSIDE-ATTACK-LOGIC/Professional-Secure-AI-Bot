from flask import Blueprint, jsonify, render_template, request

from professional_secure_ai_bot.chatbots.user_manage_chatbot import (
    user_management_answer,
)

user_manage_chatbot = Blueprint("user_manage_chatbot", __name__)


@user_manage_chatbot.route("/ask", methods=["POST"])
def ask_question():
    """This route is used to send the question for answering."""
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Question is required."}), 400
    answer = user_management_answer(question)
    return jsonify({"answer": answer})


@user_manage_chatbot.route("/chat")
def chat():
    """Renders the chat template with the right route and title."""
    return render_template(
        "base_chat.html",
        ajax_url="user_manage_chatbot.ask_question",
        chatbot_title="User Data Chatbot",
    )
