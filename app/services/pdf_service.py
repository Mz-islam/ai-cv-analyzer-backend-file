from pypdf import PdfReader
from fastapi import UploadFile, HTTPException
import os
import uuid


UPLOAD_DIR = "uploads"


def save_uploaded_pdf(file: UploadFile) -> str:
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path


def extract_text_from_pdf(file_path: str) -> str:
    try:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No readable text found in PDF. This may be a scanned image PDF."
            )

        return text.strip()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"PDF text extraction failed: {str(e)}"
        )