from abc import ABC,abstractmethod
from .command_model_note import NoteUpdateModel
from domain.notes.repository import NoteRepository,NoteConfigRepository
from domain.notes.exceptions import ExceptionLoadNote
from domain.notes.entities import Note,Config
from domain.notes.services import CorpusNoteService
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
    noteConfigRepository:NoteConfigRepository
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
    def __init__(self,unit:NoteCommandUsecaseUnitOfWork,questionService:IQuestionService,summarizerService:ISummaryService,corpusService:CorpusNoteService):

        super().__init__()
        self.corpusService = corpusService
        self.questionService = questionService
        self.summarizerService = summarizerService
        self.unit:NoteCommandUsecaseUnitOfWork = unit

    @staticmethod
    def validateFindingNote(note):
        if not(note):
            raise ExceptionLoadNote
    def makeQuestionary(self,note:NoteUpdateModel):
        config:Config = self.unit.noteConfigRepository.find_by_id(note.note_id)
        NoteCommandUseCaseImpl.validateFindingNote(config.file_ref)
        noteGetted:Note = self.unit.noteRepository.read(config.file_ref)
        
        summary = self.corpusService.extractQuestions(corpus="question")
        questions = self.corpusService.extractQuestions(corpus="summary")
        if not(all([summary,questions])):
            noteGetted.is_already_questioned = True
            noteGetted.is_already_summarized = True
            return
        noteGetted.questions =  self.questionService.make_questions(noteGetted.corpus)
        try:
            self.unit.noteRepository.update(noteGetted)
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
