from app.vectorstore.vectordb import load_vectorstore


def retrieve_chunks(query):

    vectordb = load_vectorstore()

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(query)

    return docs