from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Kanji/Hanzi Learner API")

origins = [
    "http://localhost:3000",
    "http://localhost",
    os.getenv("FRONTEND_URL", "*"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/characters")
def get_characters(limit: int = 10, skip: int = 0):
    return {
        "characters": [],
        "total": 0,
        "limit": limit,
        "skip": skip
    }

@app.post("/api/progress")
def log_progress(user_id: str, character_id: str, correct: bool):
    return {"status": "logged"}

@app.get("/api/user/{user_id}/progress")
def get_user_progress(user_id: str):
    return {
        "user_id": user_id,
        "total_learned": 0,
        "streak": 0,
        "characters": []
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
