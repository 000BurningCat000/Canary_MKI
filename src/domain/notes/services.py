from abc import ABC,abstractmethod
class CorpusNoteService(ABC):
    @abstractmethod
    @property
    def label(self) -> str:
        ...
    

    @abstractmethod
    def extractQuestions(corpus:str):
        ...