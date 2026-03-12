import os
from langchain_community.document_loaders import PyPDFLoader
from app.core.config import DOCUMENT_DIR


def load_documents():

    documents = []

    for file in os.listdir(DOCUMENT_DIR):

        if file.endswith(".pdf"):

            file_path = os.path.join(DOCUMENT_DIR, file)

            loader = PyPDFLoader(file_path)

            docs = loader.load()

            documents.extend(docs)

    return documents