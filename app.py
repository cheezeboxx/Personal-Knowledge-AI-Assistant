from src.pdf_processor import extract_pages, create_chunks
from src.embeddings import create_embeddings, create_query_embedding
from src.llm import generate_answer


import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

st.title("📚 Personal Knowledge AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize Models & Database
client_gemini = genai.Client(
    api_key= os.getenv("GEMINI_API_KEY")
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client_db = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client_db.get_or_create_collection(
    "knowledge_base"
)

# Upload PDF

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file:

    save_path = f"data/pdfs/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"{uploaded_file.name} uploaded successfully!")


    # PDF processing and creating Chunks

    page_texts = extract_pages(save_path)

    chunks, metadata_list = create_chunks(page_texts)

    # Create embeddings
    embeddings = create_embeddings(chunks)

    st.write("Embeddings generated!")

    # Store in ChromaDB
    for i, chunk in enumerate(chunks):

        try:
            collection.add(
                documents=[chunk],
                embeddings=[embeddings[i].tolist()],
                ids=[f"{uploaded_file.name}_{i}"],
                metadatas=[
                    {
                        "source": uploaded_file.name,
                        "page" : metadata_list[i]["page"],
                        "chunk_id": i
                    }
                ]
            )

        except Exception as e:
            st.error(f"Storage error : {e}")

    st.success("Stored in knowledge base!")

# Ask Question

question = st.chat_input("Ask a question...")

if question:

    st.session_state.messages.append(
        {
            "role" : "user",
            "content" : question
        }
    )
    with st.chat_message("user"):
        st.markdown(question)


    with st.spinner("Thinking..."):

        query_embedding = create_query_embedding(question)

        results = collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=5
        )

        docs = results["documents"][0]

        context = "\n\n".join(docs)

        # generating answer 
        answer = generate_answer(context, question)
        
        st.session_state.messages.append(
            {
                "role" : "assistant",
                "content" : answer
            }
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

        with st.expander("Retrieved Context"):
            st.write(context)

        st.subheader("Sources")

        shown = set()

        for meta in results["metadatas"][0]:

            source = meta["source"]

            if source not in shown:
                shown.add(source)
                page = meta.get("page", "Unknown")
                st.write(
                    f"{source}  (Page {page})"
                )