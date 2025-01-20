from  abc import ABC,abstractmethod
from domain.notes.entities import Note
from domain.notes.value_objects import NoteQuestions

class IQuestionService(ABC):
    @abstractmethod
    def make_questions(self, note: Note):
        ...

class ISummaryService(ABC):
    @abstractmethod
    def summarize_note_content(self, note: Note) -> NoteQuestions:
        ...