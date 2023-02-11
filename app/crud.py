from sqlalchemy.orm import Session
from models import tipodocumento


def get_tipodocumento(db: Session, book_id: int):
    return db.query(tipodocumento).filter(tipodocumento.id == book_id).first()
