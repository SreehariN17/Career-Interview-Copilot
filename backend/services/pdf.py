from pypdf import PdfReader

# Loads a PDF file and extracts text from it page by page 
# Returns the extracted text as a string
def extract_text(file):
    # If a filepath was passed
    if isinstance(file, str):
        reader = PdfReader(file)

    # If UploadFile was passed
    else:
        reader = PdfReader(file.file)
    
    text = ""
    
    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text 