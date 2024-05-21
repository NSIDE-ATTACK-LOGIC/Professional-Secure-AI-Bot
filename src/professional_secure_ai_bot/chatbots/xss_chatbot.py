from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from professional_secure_ai_bot.ai_tools.ai_llm import get_llm

llm = get_llm()


def chat_with_bot(user_input: str) -> str:
    """Simple chatbot that answers a question via the LLM. Used in the XSS demo."""
    prompt_template = PromptTemplate.from_template(
        "You are an intelligent chatbot. Answer the following question as accurately as possible:\n\n{input}\n"
    )
    chatbot_chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chatbot_chain.invoke({"input": user_input})

    return response
