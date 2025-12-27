import os
import pdfplumber

def load_documents(folder_path="data"):
    docs = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf"):
            text = ""
            with pdfplumber.open(os.path.join(folder_path, file)) as pdf:
                for page in pdf.pages:
                    t = page.extract_text()
                    if t:
                        text += t + "\n"
            text = text.replace("\n", " ")
            text = " ".join(text.split())
            docs.append({"id": file, "text": text})
    return docs
