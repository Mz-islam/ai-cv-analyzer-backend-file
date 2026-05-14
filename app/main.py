from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models.schemas import CVTextAnalyzeRequest
from app.services.cv_analyzer_service import analyze_text_cv, analyze_pdf_cv
from app.services.pdf_service import save_uploaded_pdf, extract_text_from_pdf
from app.repositories.cv_repository import get_analysis_history


app = FastAPI(title="Campus Mentor AI CV Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Campus Mentor AI CV Analyzer is running"
    }


@app.post("/api/cv/analyze-text")
def analyze_cv_text(request: CVTextAnalyzeRequest):
    if len(request.cv_text.strip()) < 50:
        raise HTTPException(
            status_code=400,
            detail="CV text is too short. Please provide more details."
        )

    return analyze_text_cv(
        student_id=request.student_id,
        target_track=request.target_track,
        target_role=request.target_role,
        cv_text=request.cv_text
    )


@app.post("/api/cv/analyze-pdf")
def analyze_cv_pdf(
    student_id: str = Form(...),
    target_track: str = Form(...),
    target_role: str = Form(...),
    file: UploadFile = File(...)
):
    file_path = save_uploaded_pdf(file)
    extracted_text = extract_text_from_pdf(file_path)

    if len(extracted_text.strip()) < 50:
        raise HTTPException(
            status_code=400,
            detail="Extracted CV text is too short. Please upload a readable PDF CV."
        )

    return analyze_pdf_cv(
        student_id=student_id,
        target_track=target_track,
        target_role=target_role,
        original_file_name=file.filename,
        extracted_text=extracted_text
    )


@app.get("/api/cv/history/{student_id}")
def history(student_id: str):
    return get_analysis_history(student_id)