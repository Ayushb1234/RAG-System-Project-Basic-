from langchain_community.vectorstores import Chroma
from app.ingestion.embedder import get_embedding_model
from app.core.config import VECTOR_DB_DIR


def create_vectorstore(chunks):

    embeddings = get_embedding_model()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )

    vectordb.persist()

    return vectordb


def load_vectorstore():

    embeddings = get_embedding_model()

    vectordb = Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embeddings
    )

    return vectordb