from domain.notes.repository import NoteRepository
from use_cases.notes.command_note import NoteCommandUsecaseUnitOfWork
from domain.notes.entities import Note


class NoteUnitOfWorkImpl(NoteCommandUsecaseUnitOfWork):
    noteRepository:NoteRepository
    def __init__(self):
        self.transaction_active = False
        self.backup_data = None
        super().__init__()
    def begin(self):
        self.noteRepository.read()
        
    def commit(self):
        ...
    def rollback(self):
        ...


class NoteRepositoryMarkdownImpl(NoteRepository):
    def __init__(self,filename:str):
        super().__init__()
    def read(self,note:Note):
        ...

    def find_by_id(self,id:int):
        ...

    def update(self,note:Note):
        ...

    def delete_by_id(self,id:int):
        ...
    def delete(self,note:Note):
        ...