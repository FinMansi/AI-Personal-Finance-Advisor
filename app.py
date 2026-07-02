import streamlit as st
from rag_pipeline import build_rag_pipeline

st.title("💰 Financial Q&A Assistant")
st.write("Ask me beginner-friendly finance questions!")

qa_chain = build_rag_pipeline()

user_query = st.text_input("Enter your question:")
if user_query:
    response = qa_chain.run(user_query)
    st.write("### Answer:")
    st.write(response)
