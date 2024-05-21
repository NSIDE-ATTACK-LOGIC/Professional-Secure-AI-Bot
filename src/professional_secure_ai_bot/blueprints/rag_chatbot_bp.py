from flask import Blueprint, jsonify, render_template, request

from professional_secure_ai_bot.chatbots.rag_chatbot import rag_answer

rag_chatbot = Blueprint("rag_chatbot", __name__)


@rag_chatbot.route("/ask", methods=["POST"])
def ask_question():
    """This route is used to send the question for answering."""
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Question is required."}), 400
    answer = rag_answer(question)
    return jsonify({"answer": answer})


@rag_chatbot.route("/chat")
def chat():
    """Renders the chat template with the right route and title."""
    return render_template(
        "base_chat.html",
        ajax_url="rag_chatbot.ask_question",
        chatbot_title="RAG empowered Chatbot",
    )
