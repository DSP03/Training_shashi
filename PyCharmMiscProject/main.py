"""
Master Class 5 — FastAPI, Pydantic & Unit Testing
A small, runnable "Notes" API used throughout the class demo.

Run me with:
    uvicorn main:app --reload

Then open:
    http://127.0.0.1:8000/docs      (Swagger UI)
    http://127.0.0.1:8000/redoc     (ReDoc)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Bootcamp Notes API")

# ---------------------------------------------------------------------
# In-memory "database" — good enough for a live demo
# ---------------------------------------------------------------------
_notes_db: dict[int, dict] = {
    1: {"id": 1, "title": "Welcome", "body": "This is your first note.", "tags": ["intro"]},
}
_next_id = 2


# ---------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------
class NoteIn(BaseModel):
    """Request body shape for creating a note — like a Java DTO + @Valid."""
    title: str = Field(min_length=1, max_length=100)
    body: str = Field(min_length=1)
    tags: list[str] = Field(default_factory=list, max_length=5)

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("title cannot be blank")
        return v


class NoteOut(BaseModel):
    """Response shape — separate from NoteIn so we control exactly what's returned."""
    id: int
    title: str
    body: str
    tags: list[str]


# ---------------------------------------------------------------------
# Simulated "external service" call — this is what we'll mock in tests
# ---------------------------------------------------------------------
def send_notification(note: NoteOut) -> None:
    """Pretend this calls Slack / email / a webhook somewhere external."""
    print(f"[notification] New note created: {note.title!r}")


# ---------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------
@app.get("/")
def read_root():
    return {"status": "ok"}


@app.get("/notes", response_model=list[NoteOut])
def list_notes(limit: int = 10):
    """GET /notes?limit=5 — query parameter with a default."""
    return list(_notes_db.values())[:limit]


@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    """GET /notes/1 — path parameter, automatically validated as an int."""
    note = _notes_db.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.post("/notes", response_model=NoteOut, status_code=201)
def create_note(note: NoteIn):
    """POST /notes — request body parsed & validated into a NoteIn automatically."""
    global _next_id
    new_note = {"id": _next_id, **note.model_dump()}
    _notes_db[_next_id] = new_note
    _next_id += 1

    send_notification(NoteOut(**new_note))   # the call we'll mock in tests
    return new_note


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
