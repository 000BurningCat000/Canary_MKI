from domain.notes.repository import NoteRepository,NoteConfigRepository
from use_cases.notes.command_note import NoteCommandUsecaseUnitOfWork
from domain.notes.entities import Note,Config
from .Merger import MergerModel
from pickle import loads
from hashlib import md5
from flask_sqlalchemy import SQLAlchemy
class NoteUnitOfWorkImpl(NoteCommandUsecaseUnitOfWork):
    noteRepository:NoteRepository
    noteConfigRepository:NoteConfigRepository
    def __init__(self,filepath:str):
        self.filepath = filepath
        self.transaction_active = False
        self.backup_data = None
        super().__init__()
    def begin(self):
        self.transaction_active = True

        self.backup_data:Note = self.noteRepository.read(self.filepath)
    def commit(self):
        if self.transaction_active:
            self.transaction_active = False
            self.backup_data = None
        self.noteConfigRepository.db.session.commit()

    def rollback(self):
        self.noteRepository.update(self.backup_data,self.filepath)
        
        self.noteConfigRepository.db.session.rollback()
    
class NoteConfigRepositoryImpl(NoteConfigRepository):
    def __init__(self,db:SQLAlchemy):
        self.db:SQLAlchemy = db
        super().__init__()
    def create(self,config:Config):
        self.db.session.add(config)
    def find_by_id(self,id:str) -> Config:
        try:
            config = self.db.get_or_404(Config,id)
        except:
            raise
        return config
    
    def delete_by_id(self,id:str):
        config = self.db.get_or_404(Config,id)
        self.db.session.delete(config)
    def update(self,config:Config,config_id:str):
        config = self.db.get_or_404(Config,config_id)
        if not(config):
            raise 
        config.file_ref = config.file_ref
        config.old_hashes = config.old_hashes
        config.hash_file = config.hash_file

class NoteRepositoryMarkdownImpl(NoteRepository):
    def __init__(self,merger:MergerModel):
        self.merger = merger
        super().__init__()



    def read(self,filename:str) -> Note:
        try:
            with self.merger(filename) as rds:
                corpus = rds.io.read()
                hashb = md5(bytes(rds)).hexdigest()
                summary = self.extractQuestions('summary',corpus)
                questions = self.extractQuestions('questions',corpus)
                return Note(
                    note_id=hashb,
                    summary=summary,
                    questions=questions,
                    corpus=rds.io.read())
        except Exception as e:
            raise
    def update(self,note:Note,filename:str):
        try:
            with self.merger(filename) as ads:
                ads.write(note.questions)
                ads.write(note.summary)
        except:
            ...
        ...