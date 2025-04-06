# type: ignore
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/props/{player_name}")
def get_props(player_name: str):
    # Dummy data for now
    return {
        "player": player_name,
        "stat": "rebounds",
        "line": 8.5,
        "hit_rate": "9/10",
        "confidence": "90%"
    }
