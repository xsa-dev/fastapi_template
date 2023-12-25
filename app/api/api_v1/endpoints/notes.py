from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud.crud_note import (
    get_notes,
    create_user_note,
    get_note,
    update_user_note,
    delete_user_note
)
from app.schemas.note import NoteCreate, Note, NoteUpdate
from app.models import User
from app.core.security import get_current_user

router = APIRouter()


@router.get("/", response_model=List[Note])
def read_notes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_notes(db=db, owner_id=current_user.id)


@router.post("/", response_model=Note)
def create_note(
        note: NoteCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    return create_user_note(db=db, note=note, owner_id=current_user.id)


@router.put("/{note_id}", response_model=Note)
def update_note(
        note_id: int,
        note: NoteUpdate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    if updated_note := update_user_note(
            db=db, note=note, note_id=note_id, owner_id=current_user.id
    ):
        return updated_note
    else:
        raise HTTPException(status_code=404, detail="Note not found.")


@router.delete("/{note_id}", response_model=Note)
def delete_note(
        note_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    if note := delete_user_note(
            db=db, note_id=note_id, owner_id=current_user.id
    ):
        return note
    else:
        raise HTTPException(status_code=404, detail="Note not found.")
