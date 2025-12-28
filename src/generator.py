import os
import google.generativeai as genai
import streamlit as st   # add this to read secrets

# Configure Gemini using Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(context_chunks, query):
    context = "\n\n".join([c for c, _ in context_chunks])

    prompt = f"""
Answer ONLY using the context provided below.
If answer is NOT found, respond exactly:
"Information not available in provided documents."

CONTEXT:
{context}

QUESTION: {query}
"""
    response = model.generate_content(prompt)
    return response.text
