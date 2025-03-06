import streamlit as st
from retrieval import retrieve_docs
from llm_generation import generate_answer

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("🔍 RAG-Based Chatbot")

st.markdown("### Ask me a question, and I'll fetch the most relevant information from Wikipedia before answering!")

user_query = st.text_input("💬 Your Question:")
if user_query:
    with st.spinner("Retrieving relevant documents..."):
        retrieved_docs = retrieve_docs(user_query, top_k=3)
        context = " ".join(retrieved_docs)

    with st.spinner("Generating AI response..."):
        response = generate_answer(user_query, context)

    # Display retrieved documents
    st.subheader("📄 Relevant Documents Retrieved:")
    for doc in retrieved_docs:
        st.write(f"- {doc[:300]}...")  # Show snippet

    # Display chatbot response
    st.subheader("🤖 AI Chatbot Response:")
    st.success(response)
