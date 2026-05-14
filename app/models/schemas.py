from pydantic import BaseModel
from typing import List, Dict, Optional


class CVTextAnalyzeRequest(BaseModel):
    student_id: str
    target_track: str
    target_role: str
    cv_text: str


class CVAnalysisResult(BaseModel):
    ats_score: int
    detected_skills: List[str]
    missing_skills: List[str]
    priority_feedback: Dict[str, List[str]]
    section_feedback: Dict[str, str]
    improvement_suggestions: List[str]
    roadmap: List[str]
    recommended_feature: str
    confidence_level: str
    explanation: str


class CVAnalysisResponse(BaseModel):
    analysis_id: int
    student_id: str
    target_track: str
    target_role: str
    input_type: str
    result: CVAnalysisResult