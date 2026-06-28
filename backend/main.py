from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load .env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")

# Create FastAPI app
app = FastAPI(title="EduGenie")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class Question(BaseModel):
    question: str

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to EduGenie!"}

# Ask AI route
@app.post("/ask")
def ask_ai(data: Question):
    response = model.generate_content(data.question)
    return {"answer": response.text}
@app.post("/quiz")
def generate_quiz(data: Question):
    prompt = f"""
    Generate a quiz with 5 multiple-choice questions on the topic:
    {data.question}

    Include:
    - Question
    - Four options (A, B, C, D)
    - Correct answer
    """

    response = model.generate_content(prompt)
    return {"answer": response.text}
@app.post("/summarize")
def summarize(data: Question):
    prompt = f"""
    Summarize the following text in simple and concise points:

    {data.question}
    """

    response = model.generate_content(prompt)
    return {"answer": response.text}
@app.post("/learning-path")
def learning_path(data: Question):
    prompt = f"""
    Create a beginner-to-advanced learning roadmap for:
    {data.question}

    Include:
    1. Beginner topics
    2. Intermediate topics
    3. Advanced topics
    4. Recommended projects
    """

    response = model.generate_content(prompt)
    return {"answer": response.text}