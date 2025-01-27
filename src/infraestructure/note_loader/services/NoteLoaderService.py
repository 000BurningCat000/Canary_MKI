from domain.notes.services import CorpusNoteService
from re import find
class CorpusNoteServiceImpl(CorpusNoteService):
    def __init__(self):
        self._label = "#"
        super().__init__()
    @property
    def label(self) -> str:
        return self._label 
    def extractQuestions(self,corpus:str):
        x = corpus.find(corpus,r'#' + self.label )
        if x.end() == -1:
            return ''
        update_corpus = corpus[x.end():]
        endOfSection = update_corpus.find(f'#{self.label}')
        if endOfSection == -1:
            return update_corpus
        return update_corpus[:endOfSection]#