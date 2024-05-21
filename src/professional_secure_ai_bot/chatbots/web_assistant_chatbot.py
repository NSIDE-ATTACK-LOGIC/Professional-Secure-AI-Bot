from professional_secure_ai_bot.chatbots.base_chatbot import chatbot_answer
from professional_secure_ai_bot.tools.file_management import (
    get_file_content,
    get_filenames_in_directory,
)
from professional_secure_ai_bot.tools.web_content import get_web_content


def web_assistant_answer(question: str) -> str:
    """Uses the base_chatbot.py to implement a chatbot that can access local files in the textfiles directory and browse any URL via the requests library."""
    system_prompt = """You are a helpful and capable assistant. 
            You can access webpages via URL and you can access local files by filename. You can list files in the files directory."""

    tools = [get_filenames_in_directory, get_file_content, get_web_content]

    answer = chatbot_answer(question=question, tools=tools, system_prompt=system_prompt)

    return answer
