from . import dataclass
from .value_objects import Question_maked
from domain.IA.entities import IA
@dataclass
class Note:
    note_id:str
    corpus:str# cuerpo de la nota
    summary:str
    questions:list[Question_maked]|None
    def __eq__(self,note):
        return note.note_id == self.note_id
    def get_content(self):
        return self.corpus
    def is_already_summarized(self):
        if not(self.summary != ""):
            return False
        return True
    def is_already_questioned(self):
        if not(self.questions):
            return False
        return True
     
