import json
from app.database.mysql_connection import get_connection


def save_cv_analysis(
    student_id: str,
    target_track: str,
    target_role: str,
    input_type: str,
    original_file_name: str,
    extracted_cv_text: str,
    result: dict
) -> int:
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO cv_analysis (
        student_id,
        target_track,
        target_role,
        input_type,
        original_file_name,
        extracted_cv_text,
        ats_score,
        detected_skills,
        missing_skills,
        priority_feedback,
        section_feedback,
        improvement_suggestions,
        roadmap,
        recommended_feature,
        confidence_level,
        explanation
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        student_id,
        target_track,
        target_role,
        input_type,
        original_file_name,
        extracted_cv_text,
        result.get("ats_score"),
        json.dumps(result.get("detected_skills", [])),
        json.dumps(result.get("missing_skills", [])),
        json.dumps(result.get("priority_feedback", {})),
        json.dumps(result.get("section_feedback", {})),
        json.dumps(result.get("improvement_suggestions", [])),
        json.dumps(result.get("roadmap", [])),
        result.get("recommended_feature"),
        result.get("confidence_level"),
        result.get("explanation")
    )

    cursor.execute(query, values)
    connection.commit()

    analysis_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return analysis_id


def get_analysis_history(student_id: str):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT 
        id,
        student_id,
        target_track,
        target_role,
        input_type,
        original_file_name,
        ats_score,
        detected_skills,
        missing_skills,
        priority_feedback,
        section_feedback,
        improvement_suggestions,
        roadmap,
        recommended_feature,
        confidence_level,
        explanation,
        created_at
    FROM cv_analysis
    WHERE student_id = %s
    ORDER BY created_at DESC
    """

    cursor.execute(query, (student_id,))
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows