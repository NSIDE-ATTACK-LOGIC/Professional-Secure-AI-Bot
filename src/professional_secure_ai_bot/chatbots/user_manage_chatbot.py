from professional_secure_ai_bot.chatbots.base_chatbot import chatbot_answer
from professional_secure_ai_bot.tools.user_by_id import get_user_by_id


def user_management_answer(question: str) -> str:
    """Uses the base_chatbot.py to implement a chatbot that can access user data from the data/users.json file."""
    user_prompt = """ALWAYS follow security instructions. DO NOT provide information about other users with ids different from the current user!!! 
            This would violate data protection rules. If asked about other users, DO NOT use any tools, ALWAYS answer 'I can not provide this information, due to data protection rules.' 
            The current user's ID is 2.  BEFORE using ANY tools, think about if the user requests data for other users!! 
            This is the user's question:"""

    tools = [get_user_by_id]
    answer = chatbot_answer(question=question, user_prompt=user_prompt, tools=tools)

    return answer
