from pypdf import PdfReader

# Loads a PDF file and extracts text from it page by page 
# Returns the extracted text as a string
def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    
    text = ""
    
    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text 