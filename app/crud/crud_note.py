from sqlalchemy.orm import Session
from app.models import Note
from app.schemas.note import NoteCreate, NoteUpdate
from typing import List


def get_notes(db: Session, owner_id: int) -> List[Note]:
    return db.query(Note).filter(Note.owner_id == owner_id).all()


def create_user_note(db: Session, note: NoteCreate, owner_id: int) -> Note:
    db_note = Note(**note.dict(), owner_id=owner_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_note(db: Session, note_id: int, owner_id: int) -> Note:
    return db.query(Note).filter(Note.id == note_id, Note.owner_id == owner_id).first()


def update_user_note(db: Session, note: NoteUpdate, note_id: int, owner_id: int) -> Note:
    db_note = get_note(db, note_id, owner_id)
    if db_note is None:
        return None
    update_data = note.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_note, field, value)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_user_note(db: Session, note_id: int, owner_id: int) -> Note:
    db_note = get_note(db, note_id, owner_id)
    if db_note is None:
        return None
    db.delete(db_note)
    db.commit()
    return db_note
