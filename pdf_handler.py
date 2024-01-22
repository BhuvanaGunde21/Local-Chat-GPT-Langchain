import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from app import add_documents_to_db
import pypdfium2
from pdf_handler import get_document_chunks
sys.path.append()

print("Before import statement")
from pdf_handler import get_document_chunks, get_pdf_texts
print("After import statement")


def get_pdf_texts(pdfs_bytes_list):
    return [extract_text_from_pdf(pdf_bytes.getvalue()) for pdf_bytes in pdfs_bytes_list]

def extract_text_from_pdf(pdf_bytes):
    pdf_file = pypdfium2.PdfDocument(pdf_bytes)
    return "\n".join(pdf_file.get_page(page_number).get_textpage().get_text_range() for page_number in range(len(pdf_file)))
    
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=50, separators=["\n", "\n\n"])
    return splitter.split_text(text)

def get_document_chunks(text_list):
    documents = []
    for text in text_list:
        for chunk in get_text_chunks(text):
            documents.append(Document(page_content = chunk))
    return documents

add_documents_to_db
get_document_chunks 
get_pdf_texts