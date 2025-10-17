from fastapi import FastAPI, Query
from qa_engine import process_question

app = FastAPI(title="Project Samarth API", description="Intelligent Q&A for Agriculture & Climate Data")

@app.get("/")
def home():
    return {"message": "Project Samarth API running"}

@app.get("/ask")
def ask(question: str = Query(..., description="Enter a natural language question about Indian agriculture and climate data")):
    result = process_question(question)
    if "answer" not in result:
        result = {"answer": "Unexpected backend error."}
    return result
