from . import dataclass
from .value_objects import Question_maked

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
     
@dataclass
class Config:
    hash_file: str
    old_hashes: list[str]
    file_ref:str
    def add_old_hash(self, new_hash: str):
        self.old_hashes.append(new_hash)