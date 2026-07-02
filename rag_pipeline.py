from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def build_rag_pipeline():
    # Load embeddings
    embeddings = OpenAIEmbeddings()

    # Load your finance FAQs dataset
    # Example: [{"question": "What is compound interest?", "answer": "..."}]
    import json
    with open("data/finance_faqs.json", "r") as f:
        docs = json.load(f)

    # Convert to FAISS vector store
    texts = [d["answer"] for d in docs]
    metadatas = [{"question": d["question"]} for d in docs]
    vectorstore = FAISS.from_texts(texts, embeddings, metadatas=metadatas)

    # Build RAG pipeline
    retriever = vectorstore.as_retriever()
    llm = OpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)

    return qa_chain
