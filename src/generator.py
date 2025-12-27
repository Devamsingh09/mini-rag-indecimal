import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
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
