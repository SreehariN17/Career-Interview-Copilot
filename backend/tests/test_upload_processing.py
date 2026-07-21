from services.pdf import extract_text

from fastapi import UploadFile
from pathlib import Path 

file_path = Path("data/sample_resume.pdf")

with open(file_path, "rb") as f: 
    upload_file = UploadFile(filename="sample_resume.pdf", file=f)
    text = extract_text(upload_file)

print(text[:1000])