import json
from google import genai
from app.config.settings import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_cv_with_gemini(target_track: str, target_role: str, cv_text: str) -> dict:
    prompt = f"""
You are an expert AI CV Analyzer for university students.

Analyze this CV based on the selected target track and target role.

Target Track: {target_track}
Target Role: {target_role}

CV Text:
{cv_text}

Return ONLY valid JSON. Do not use markdown. Do not add explanation outside JSON.

Use this exact JSON structure:

{{
  "ats_score": 0,
  "detected_skills": [],
  "missing_skills": [],
  "priority_feedback": {{
    "high": [],
    "medium": [],
    "low": []
  }},
  "section_feedback": {{
    "summary": "",
    "education": "",
    "skills": "",
    "projects": "",
    "experience": "",
    "achievements": "",
    "certificates": "",
    "contact_links": ""
  }},
  "improvement_suggestions": [],
  "roadmap": [],
  "recommended_feature": "",
  "confidence_level": "",
  "explanation": ""
}}

Rules:
- ats_score must be between 0 and 100.
- detected_skills must come from the CV only.
- missing_skills should be based on the target role.
- For Industry Track, focus on technical skills, projects, GitHub, deployment, internship readiness.
- For Academia Track, focus on research interest, publication, academic project, CGPA, conference/workshop.
- For Startup Track, focus on leadership, product idea, teamwork, business competition, pitching.
- Give practical suggestions for a university student.
- Roadmap should contain 5 short action steps.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    raw_text = response.text.strip()

    if raw_text.startswith("```json"):
        raw_text = raw_text.replace("```json", "").replace("```", "").strip()
    elif raw_text.startswith("```"):
        raw_text = raw_text.replace("```", "").strip()

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        raise ValueError(f"Gemini did not return valid JSON: {raw_text}")