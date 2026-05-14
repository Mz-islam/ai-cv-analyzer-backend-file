# AI CV Analyzer Backend

<img width="1400" height="650" alt="ai-cv-analyzer-banner" src="https://github.com/user-attachments/assets/d782fbbe-e2e9-4054-8f8d-b3d9cf84e9bf" />

A standalone **AI CV Analyzer Backend** 
This backend analyzes student CVs using **Gemini API**. It supports both **Paste CV Text** and **PDF Upload**. The analysis result is saved in a local **MySQL database** using **XAMPP/phpMyAdmin**.

---

## Project Overview

The goal of this project is to help students improve their CV based on their selected career track and target role.

The system can analyze:

- Pasted CV text
- Uploaded PDF CV
- Target track
- Target role
- ATS score
- Detected skills
- Missing skills
- Priority feedback
- Section-wise CV feedback
- Improvement suggestions
- Personalized roadmap
- Recommended next feature
- Confidence level and explanation

---

## Tech Stack

| Part | Technology |
|---|---|
| Backend Framework | Python FastAPI |
| AI API | Gemini API |
| PDF Text Extraction | pypdf |
| Database | MySQL |
| Local Database Tool | XAMPP/phpMyAdmin |
| API Testing | Swagger UI |
| Environment Variables | python-dotenv |
| Future Integration | Java Spring Boot + MongoDB Atlas |

---

## Features

### Phase 1: Paste CV Text

Students can paste their CV text and get AI-based CV analysis.

### Phase 2: PDF Upload

Students can upload a PDF CV. The backend extracts text from the PDF and sends it to Gemini API for analysis.

### AI Analysis Output

The AI returns a structured result including:

- ATS score
- Detected skills
- Missing skills
- Priority-based feedback
- Section-wise feedback
- Improvement suggestions
- Roadmap
- Recommended next feature
- Confidence level
- Explanation

---

## Project Architecture

text
User / Frontend
   |
   | Paste CV text OR Upload PDF
   v
FastAPI Backend
   |
   | If PDF, extract text using pypdf
   v
Gemini API
   |
   | Return structured JSON analysis
   v
FastAPI Backend
   |
   | Save result
   v
MySQL Database
   |
   v
Return result to frontend


## Folder Structure

```text
ai-cv-analyzer/
│
├── app/
│   ├── main.py
│   ├── config/
│   │   └── settings.py
│   ├── database/
│   │   └── mysql_connection.py
│   ├── models/
│   │   └── schemas.py
│   ├── repositories/
│   │   └── cv_repository.py
│   └── services/
│       ├── cv_analyzer_service.py
│       ├── gemini_service.py
│       └── pdf_service.py
│
├── uploads/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup
1. Clone the Repository
git clone https://github.com/Mz-islam/ai-cv-analyzer-backend-file.git
cd ai-cv-analyzer-backend-file
2. Create Virtual Environment
python -m venv .venv

## Activate virtual environment on Windows PowerShell:

.venv\Scripts\activate

** If PowerShell blocks activation, run:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\activate

After activation, terminal should look like this:

(.venv) PS D:\...\ai-cv-analyzer>

3. Install Required Packages
pip install -r requirements.txt

If you want to install manually:

pip install fastapi uvicorn python-dotenv mysql-connector-python pydantic google-genai pypdf python-multipart
Environment Variables

## Create a .env file in the project root folder.

GEMINI_API_KEY=your_gemini_api_key_here

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=campus_cv_analyzer

## Important:

Do not upload .env to GitHub.
Keep your Gemini API key private.
.env is ignored using .gitignore.
Database Setup

## Start XAMPP:

Apache: Start
MySQL: Start

## Open phpMyAdmin:

http://localhost/phpmyadmin

Then go to the SQL tab and run this:

CREATE DATABASE IF NOT EXISTS campus_cv_analyzer;

USE campus_cv_analyzer;

CREATE TABLE IF NOT EXISTS cv_analysis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(100) NOT NULL,
    target_track VARCHAR(100) NOT NULL,
    target_role VARCHAR(150) NOT NULL,
    input_type VARCHAR(50) NOT NULL,
    original_file_name VARCHAR(255),
    extracted_cv_text LONGTEXT NOT NULL,
    ats_score INT,
    detected_skills JSON,
    missing_skills JSON,
    priority_feedback JSON,
    section_feedback JSON,
    improvement_suggestions JSON,
    roadmap JSON,
    recommended_feature VARCHAR(255),
    confidence_level VARCHAR(100),
    explanation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Run the Project

Run this command from the project root folder:

python -m uvicorn app.main:app --reload --port 8000

If the server starts successfully, you will see something like:

Uvicorn running on http://127.0.0.1:8000
Application startup complete.

Open the home route:

http://127.0.0.1:8000

Open Swagger UI:

http://127.0.0.1:8000/docs

Swagger UI is used to test the API endpoints easily.
