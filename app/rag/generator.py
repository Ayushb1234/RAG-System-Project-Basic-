from langchain_groq import ChatGroq
from app.core.config import GROQ_API_KEY
from app.core.prompt_templates import PROMPT_TEMPLATE


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=GROQ_API_KEY
)


def generate_answer(context, question):

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content