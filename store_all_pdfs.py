import os

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

try:
    client.delete_collection("knowledge_base")
except:
    pass

collection = client.create_collection(
    name="knowledge_base"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


pdf_folder = "data/pdfs"

for pdf_file in os.listdir(pdf_folder) :
    if not pdf_file.endswith(".pdf"):
        continue

    print(f"\nProcessing {pdf_file}")

    pdf_path = os.path.join(
        pdf_folder, 
        pdf_file
    )

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100
    )

    chunks = splitter.split_text(text)

    print(f"chunks created : {len(chunks)}")

    embeddings = model.encode(chunks)

    for i, chunks in enumerate(chunks):

        collection.add(
            ids = [f"{pdf_file}_{i}"],
            documents = [chunks],
            embeddings = [embeddings[i].tolist()],
            metadatas = [
                {
                    "source" : pdf_file,
                    "chunk_id" : i
                }
            ]
        )

print("\nKnowledge based created!")
print(
    "Total chunks:", collection.count()
)
