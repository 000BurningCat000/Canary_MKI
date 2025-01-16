from . import dataclass
from .value_objects import Question_maked

@dataclass
class Note:
    note_id:str
    corpus:str# cuerpo de la nota
    summary:str
    questions:list[Question_maked]
    def __eq__(self,note):
        return note.note_id == self.note_id
