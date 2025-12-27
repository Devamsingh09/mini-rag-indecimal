

# 🏗️ Mini-RAG — Construction Knowledge Assistant (Local Streamlit App)

A Retrieval-Augmented Generation (RAG)-based AI assistant that answers construction-related questions **strictly using internal company documents** — pricing sheets, sanitary & flooring allowances, policies, workflows, etc.

This project is developed for **Indecimal Construction Marketplace** as part of a mini-project assignment.

---

## 🎯 Project Goal

To demonstrate foundational RAG concepts by building a chatbot that:

✔ Loads internal PDFs and converts them into embeddings
✔ Stores embeddings in a FAISS vector store for fast retrieval
✔ Retrieves only relevant chunks on query
✔ Generates answers **grounded strictly in retrieved text** using Gemini-2.5 Flash
✔ Shows the retrieved evidence above every answer
✔ Prevents hallucinations — if answer is missing, responds:
**"Information not available in provided documents."**

---

## 🧰 Tech Stack

| Component   | Library / Tool                           |
| ----------- | ---------------------------------------- |
| LLM         | Google Gemini-2.5-Flash                  |
| Embeddings  | Sentence-Transformers (all-MiniLM-L6-v2) |
| Vector DB   | FAISS CPU                                |
| PDF Parsing | pdfplumber                               |
| UI          | Streamlit                                |
| Env Config  | python-dotenv                            |

---

## 📦 Local Installation Guide

> 🧠 This app is meant to **run locally** — no internet deployment is required for assignment submission.

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/mini-rag-indecimal.git
cd mini-rag-indecimal
```

### 2️⃣ Create & Activate Virtual Environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate  # macOS / Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Key

A `.env.example` file is provided.

➡️ Duplicate & rename it to `.env`:

```
cp .env.example .env      # mac / linux
rename .env.example .env  # windows
```

Then open `.env` and add:

```
GEMINI_API_KEY=your_api_key_here
```

You can generate a free key at → [https://aistudio.google.com/](https://aistudio.google.com/)

### 5️⃣ Add Your PDFs

Place your internal construction documents inside the `data/` folder:

```
data/doc1_clean.pdf
data/doc2_clean.pdf
data/doc3_clean.pdf
```

📌 File names can change — loader automatically processes *any* PDF.

### 6️⃣ (First-time setup only) Rebuild Embeddings

```bash
rm -rf vector_store/
```

### 7️⃣ Run Local Chatbot

```bash
streamlit run app.py
```

Open browser → [http://localhost:8501](http://localhost:8501)
You will see a chatbot UI that:

* shows retrieved PDF chunks
* then gives final answer grounded in those chunks

---

## 🧪 Example Correct Outputs

During validation, the system answered the following correctly:

| Question                                           | Example Answer                                              |
| -------------------------------------------------- | ----------------------------------------------------------- |
| "What is the flooring allowance for Premier tier?" | Tiles/granite up to ₹100/sqft                               |
| "What is the interior painting process?"           | 2-coat JK Putty + Primer + 2-coat Emulsion                  |
| "How does escrow payment work?"                    | Money held, released only after stage verification          |
| "Is maintenance provided?"                         | Zero-cost maintenance includes plumbing, crack repair, etc. |

Hallucination behavior verified — questions not supported in docs return:

```
"Information not available in provided documents."
```

---

## 📂 Folder Layout (Reference)

```
mini_rag/
 ├── app.py
 ├── requirements.txt
 ├── .env.example
 ├── README.md
 │
 ├── data/
 │    ├── *.pdf                # internal construction docs go here
 │
 ├── vector_store/             # auto-generated embeddings
 │
 └── src/
      ├── rag_pipeline.py
      ├── load_docs.py
      ├── embedder.py
      ├── retriever.py
      ├── generator.py
```

---

## 🔁 Updating Documents Later

If you replace or add PDFs in `/data/`, re-generate embeddings:

```bash
rm -rf vector_store/
streamlit run app.py
```

---

## 🧩 Notes

* App runs fully locally → only Gemini API call requires internet
* Cleaned PDFs improve retrieval quality
* This repository demonstrates RAG fundamentals — not production security or scaling

---

## 👤 Author

**Devam Singh**
B.Tech CSE (DSAI), 2026
📧 [devamsingh0009@gmail.com](mailto:devamsingh0009@gmail.com)
🔗 GitHub: [https://github.com/Devamsingh09](https://github.com/Devamsingh09)
🔗 LinkedIn: [https://linkedin.com/in/devam-singh-248025265/](https://linkedin.com/in/devam-singh-248025265/)


Just say:
👉 **add diagram** or **add screenshots**
