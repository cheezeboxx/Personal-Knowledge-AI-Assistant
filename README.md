# 📚 Personal Knowledge AI Assistant

### Chat with your PDFs using RAG, ChromaDB, Sentence Transformers, and Google Gemini

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions. The system retrieves relevant document chunks using semantic search and generates grounded answers using Google's Gemini LLM.

</div>

---

## 🚀 Features

* 📄 Upload and process PDF documents
* ✂️ Automatic text chunking
* 🧠 Semantic search using Sentence Transformers
* 🗄️ Vector storage with ChromaDB
* 🤖 AI-powered answers using Google Gemini
* 📚 Source-aware responses
* 📍 Page-level citations
* 💬 Chat-style interface using Streamlit
* 🔍 View retrieved context for transparency and debugging

---

## 🏗️ System Architecture

```text
PDF Upload
    │
    ▼
Text Extraction
    │
    ▼
Chunking
    │
    ▼
Embeddings Generation
    │
    ▼
ChromaDB Vector Store
    │
    ▼
Semantic Search
    │
    ▼
Retrieved Context
    │
    ▼
Gemini LLM
    │
    ▼
Answer + Sources
```

---

## 🛠️ Tech Stack

| Technology               | Purpose               |
| ------------------------ | --------------------- |
| Python                   | Core Development      |
| Streamlit                | User Interface        |
| ChromaDB                 | Vector Database       |
| Sentence Transformers    | Text Embeddings       |
| Google Gemini            | Large Language Model  |
| PyPDF                    | PDF Processing        |
| LangChain Text Splitters | Document Chunking     |
| dotenv                   | Environment Variables |

---

## 📂 Project Structure

```text
Personal-Knowledge_AI
│
├── app.py
│
├── src
│   ├── embeddings.py
│   ├── llm.py
│   └── pdf_processor.py
│
├── data
│   └── pdfs
│
├── chroma_db
│
├── store_all_pdfs.py
├── store_embeddings.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/cheezeboxx/Personal-Knowledge-AI-Assistant.git
cd Personal-Knowledge-AI-Assistant
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

You can obtain a Gemini API key from Google AI Studio.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📖 Usage

### Upload a PDF

Upload any PDF document through the Streamlit interface.

### Ask Questions

Examples:

* What is Numerical Differentiation?
* Explain Newton's Forward Difference Formula.
* Summarize Chapter 3.
* What are the advantages of interpolation?

### View Sources

The application displays:

* Source document name
* Page number
* Retrieved context

to improve transparency and answer reliability.

---

## 🧠 How It Works

1. User uploads a PDF.
2. PDF text is extracted using PyPDF.
3. Text is divided into overlapping chunks.
4. Chunks are converted into vector embeddings.
5. Embeddings are stored in ChromaDB.
6. User submits a question.
7. The question is embedded and used for semantic retrieval.
8. Relevant chunks are retrieved.
9. Retrieved context is sent to Gemini.
10. Gemini generates an answer grounded in the uploaded documents.

---

## 📸 Screenshots

### Interface
<img width="1919" height="838" alt="image" src="https://github.com/user-attachments/assets/cece8537-a133-4771-b22c-6a15530f2262" />

### PDF Upload

<img width="1086" height="809" alt="image" src="https://github.com/user-attachments/assets/65cf7f06-d73a-4b47-a5e0-50b2f047b783" />

### Question Answering

<img width="1056" height="818" alt="image" src="https://github.com/user-attachments/assets/9b55e992-0e63-4a5c-8dd2-5e5e8ded972b" />

### Retrieved Context

<img width="872" height="817" alt="image" src="https://github.com/user-attachments/assets/8c06008b-1604-464e-8d46-e2ddf2c8c5e7" />

---

## 🔮 Future Improvements

* Chat memory and conversation history
* PDF summarization
* Hybrid search (keyword + semantic)
* Document comparison
* User authentication
* Cloud deployment
* Citation highlighting inside answers
* Support for DOCX, PPTX, and TXT files

---

## 🎯 Learning Outcomes

Through this project I gained experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Embedding Models
* Large Language Models (LLMs)
* Streamlit Application Development
* Modular Software Design
* Git and GitHub

---

## 👨‍💻 Author

**Akshaj Dhadwal**

Mathematics & Computing Student | Aspiring Data Scientist

GitHub: https://github.com/cheezeboxx

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
