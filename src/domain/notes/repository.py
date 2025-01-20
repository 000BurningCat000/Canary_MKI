from abc import ABC,abstractmethod
from domain.notes.repository import Note
class NoteRepository(ABC):
    ...
    @abstractmethod
    def read(self,note:Note) -> Note:
        ...
    @abstractmethod
    def find_by_id(self,id:int):
        ...
    @abstractmethod
    def update(self,note:Note):
        ...
    @abstractmethod
    def delete_by_id(self,id:int):
        ...
    @abstractmethod
    def delete(self,note:Note):
        ...


