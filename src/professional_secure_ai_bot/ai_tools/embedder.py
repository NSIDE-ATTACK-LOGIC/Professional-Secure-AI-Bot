from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings

# Establishes one central place for the embedder, to make it adjustable


def get_embedder() -> SpacyEmbeddings:
    """Returns the embedder, allows for a central place to change it if needed."""
    embedder = SpacyEmbeddings(model_name="en_core_web_sm")
    return embedder
