from pydantic import BaseModel, Field


class NoteBase(BaseModel):
    text: str = Field(..., example="Remember to buy milk.")


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    pass


class NoteInDBBase(NoteBase):
    id: int = Field(..., example=1)

    class Config:
        orm_mode = True


class Note(NoteInDBBase):
    pass


class NoteInDB(NoteInDBBase):
    owner_id: int
