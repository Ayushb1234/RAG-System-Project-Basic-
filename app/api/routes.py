from fastapi import APIRouter
from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer

router = APIRouter()


@router.post("/ask")
def ask_question(question: str):

    docs = retrieve_chunks(question)

    context = "\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, question)

    return {"answer": answer}