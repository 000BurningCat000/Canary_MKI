from abc import ABC,abstractmethod
from domain.notes.entities import Note,Config

class NoteConfigRepository(ABC):
    @abstractmethod
    def create(self,config:Config):
        ...
    @abstractmethod
    def update(self,id:str,config:Config,config_id:str):
        ...
    @abstractmethod
    def find_by_id(self,id:str):
        ...
    @abstractmethod
    def delete_by_id(self,id:str):
        ...
class NoteRepository(ABC):
    @abstractmethod
    def read(self,filename:str) -> Note:
        ...
    @abstractmethod
    def update(self,note:Note,filename:str):
        ...