from dataclasses import dataclass
@dataclass
class NoteUpdateModel:
    note_id:int
    sumary:str
    questions:str