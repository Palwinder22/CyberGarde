
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text  # ✅ Import this
from app.db.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/health/db")
def db_health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  # ✅ Wrap SQL in text()
        return {"status": "Database is connected"}
    except SQLAlchemyError as e:
        return {"status": "Database is NOT connected", "error": str(e)}
