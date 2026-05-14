from app.services.gemini_service import analyze_cv_with_gemini
from app.repositories.cv_repository import save_cv_analysis


def analyze_text_cv(student_id: str, target_track: str, target_role: str, cv_text: str):
    result = analyze_cv_with_gemini(
        target_track=target_track,
        target_role=target_role,
        cv_text=cv_text
    )

    analysis_id = save_cv_analysis(
        student_id=student_id,
        target_track=target_track,
        target_role=target_role,
        input_type="text",
        original_file_name=None,
        extracted_cv_text=cv_text,
        result=result
    )

    return {
        "analysis_id": analysis_id,
        "student_id": student_id,
        "target_track": target_track,
        "target_role": target_role,
        "input_type": "text",
        "result": result
    }


def analyze_pdf_cv(
    student_id: str,
    target_track: str,
    target_role: str,
    original_file_name: str,
    extracted_text: str
):
    result = analyze_cv_with_gemini(
        target_track=target_track,
        target_role=target_role,
        cv_text=extracted_text
    )

    analysis_id = save_cv_analysis(
        student_id=student_id,
        target_track=target_track,
        target_role=target_role,
        input_type="pdf",
        original_file_name=original_file_name,
        extracted_cv_text=extracted_text,
        result=result
    )

    return {
        "analysis_id": analysis_id,
        "student_id": student_id,
        "target_track": target_track,
        "target_role": target_role,
        "input_type": "pdf",
        "original_file_name": original_file_name,
        "result": result
    }