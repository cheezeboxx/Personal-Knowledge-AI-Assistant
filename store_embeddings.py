from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

# Read PDF
reader = PdfReader("data/pdfs/Numerical Differentiation.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(text)

print("Total chunks:", len(chunks))

# Create embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

# Create Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="numerical_notes"
)

# Store chunks
for i, chunk in enumerate(chunks):
    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embeddings[i].tolist()],
        metadatas=[{
            "source": "Numerical Differentiation.pdf",
            "chunk_id": i
        }]
    )
    
print("Stored successfully!")