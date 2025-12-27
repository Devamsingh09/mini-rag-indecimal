import streamlit as st
from src.rag_pipeline import MiniRAG

st.title("🏗 Construction Knowledge Assistant – Mini RAG")

@st.cache_resource
def load_rag():
    return MiniRAG()

rag = load_rag()

query = st.text_input("Ask a question based on Indecimal documents:")

if st.button("Ask"):
    retrieved, answer = rag.ask(query)

    st.subheader("📌 Retrieved Context")
    for chunk, doc in retrieved:
        st.code(f"[From {doc}] — {chunk}")

    st.subheader("🤖 Final Answer")
    st.success(answer)
