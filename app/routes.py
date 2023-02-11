from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import tipodocuSchema, Request, Response, RequestBook

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{id}")
async def get_tipodocumento(skip: int = 0, db: Session = Depends(get_db)):
    _books = crud.get_tipodocumento(db, skip)
    return Response(status="Ok", code="200", message="Se encontró el resultado", result=_books)
