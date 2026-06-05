from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader


def extract_pages(save_path):

    reader = PdfReader(save_path)
    page_texts = []

    for page_num, page in enumerate(reader.pages, start = 1):
        page_text = page.extract_text()

        if page_text:
            page_texts.append(
                {
                    "page" : page_num,
                    "text" : page_text
                }
            )
    return page_texts



def create_chunks(page_texts):
    
    # Chunk PDF
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []
    metadata_list = []

    for page_data in page_texts:
        
        page_number = page_data["page"]

        page_chunks = splitter.split_text(
            page_data["text"]
        )

        for chunk in page_chunks:
            chunks.append(chunk)

            metadata_list.append(
                {
                    # "source" : uploaded_file.name,
                    "page" : page_number
                }
            )
    return chunks, metadata_list
        