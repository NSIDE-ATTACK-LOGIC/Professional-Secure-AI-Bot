import os
import shutil

import pkg_resources
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

from professional_secure_ai_bot.ai_tools.embedder import get_embedder

embedder = get_embedder()


def init_chroma_db() -> None:
    """Initializes and resets the Chroma DB."""

    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")

    # Load documentation to file
    file_name = pkg_resources.resource_filename(
        "professional_secure_ai_bot.data_tools", "notes.txt"
    )
    raw_documents = TextLoader(file_name).load()
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
    documents = text_splitter.split_documents(raw_documents)
    Chroma.from_documents(documents, embedder, persist_directory="./chroma_db")


def add_to_chroma(text: str) -> None:
    """Adds a given text to the Chroma DB."""

    # Creates the documents that are normally created by the loader
    metadata = {"source": "User Input"}
    documents = [Document(page_content=text, metadata=metadata)]
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
    documents = text_splitter.split_documents(documents)
    Chroma.from_documents(documents, embedder, persist_directory="./chroma_db")


def do_similarity_search(query: str) -> list[object]:
    """Performs similarity search with the Chroma DB on disk."""
    db3 = Chroma(persist_directory="./chroma_db", embedding_function=embedder)
    docs = db3.similarity_search(query)
    return docs
