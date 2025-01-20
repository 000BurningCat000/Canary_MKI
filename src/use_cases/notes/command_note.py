from abc import ABC,abstractmethod
from .command_model_note import NoteUpdateModel
from domain.notes.repository import NoteRepository
from domain.notes.exceptions import ExceptionLoadNote
from domain.notes.entities import Note
from use_cases.ia.services.NoteIAService import IQuestionService,ISummaryService
class NoteCommandUsecase(ABC):

    @abstractmethod
    def makeSummary(self,note:NoteUpdateModel):
        ...
    @abstractmethod
    def makeQuestionary(self,note:NoteUpdateModel):
        ...

class NoteCommandUsecaseUnitOfWork(ABC):
    noteRepository:NoteRepository
    @abstractmethod
    def begin(self):
        ...
    @abstractmethod
    def commit(self):
        ...
    @abstractmethod
    def rollback(self):
        ...

class NoteCommandUseCaseImpl(NoteCommandUsecase):
    def __init__(self,unit:NoteCommandUsecaseUnitOfWork,questionService:IQuestionService,summarizerService:ISummaryService):

        super().__init__()
        self.questionService = questionService
        self.summarizerService = summarizerService
        self.unit:NoteCommandUsecaseUnitOfWork = unit
    @staticmethod
    def validateFindingNote(note):
        if not(note):
            raise ExceptionLoadNote
    def makeQuestionary(self,note:NoteUpdateModel):
        resp:Note = self.unit.noteRepository.find_by_id(note.note_id)
        NoteCommandUseCaseImpl.validateFindingNote(resp)
        resp.questions =  self.questionService.make_questions(resp.corpus)
        try:
            self.unit.noteRepository.update(resp)
            self.unit.commit()
        except Exception as e:
            self.unit.rollback()
            raise 
    def makeSummary(self, note):
        resp:Note = self.unit.noteRepository.find_by_id(note.note_id)
        NoteCommandUseCaseImpl.validateFindingNote(resp)
        resp.summary = self.summarizerService.summarize_note_content(resp.corpus)
        try:
            self.unit.noteRepository.update(resp)
            self.unit.commit()
        except Exception as e:
            self.unit.rollback()
            raise 
