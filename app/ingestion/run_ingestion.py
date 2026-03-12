from app.ingestion.loader import load_documents
from app.ingestion.text_splitter import split_documents
from app.vectorstore.vectordb import create_vectorstore


def run_ingestion():

    print("📄 Loading documents...")

    documents = load_documents()

    print("Number of documents loaded:", len(documents))

    print("✂️ Splitting documents...")

    chunks = split_documents(documents)

    print("Number of chunks created:", len(chunks))

    print("🧠 Creating vector database...")

    create_vectorstore(chunks)

    print("✅ Ingestion completed!")


if __name__ == "__main__":
    run_ingestion()