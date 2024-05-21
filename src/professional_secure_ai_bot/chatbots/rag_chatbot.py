from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from professional_secure_ai_bot.ai_tools.ai_llm import get_llm
from professional_secure_ai_bot.ai_tools.embedder import get_embedder

llm = get_llm()

embedder = get_embedder()


def rag_answer(question: str) -> str:
    """Uses the base_chatbot.py to implement a chatbot that can access a vectorstore."""
    vectorstore = Chroma(embedding_function=embedder, persist_directory="./chroma_db")

    # Retrieve and generate using the relevant snippets of the text.
    retriever = vectorstore.as_retriever()
    prompt = PromptTemplate.from_template(
        """Answer the following question {question} by using the following context.
    Context: {context}
    Answer:
    
    """
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain.invoke(question)
