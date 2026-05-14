# AI CV Analyzer Backend

![AI CV Analyzer Banner](./ai-cv-analyzer-banner.png)

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

```text
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
