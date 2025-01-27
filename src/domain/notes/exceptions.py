class ExceptionLoadNote(Exception):
    message:str = 'Note cant be loaded!'
    def __str__(self):
        return ExceptionLoadNote.message
class ExceptionConfigLoadError(Exception):
    message:str = 'Config load Error'
    def __str__(self):
        return ExceptionLoadNote.message
class ExceptionConfigDumpsError(Exception):
    message:str = 'Error while dumpling the configs'
    def __str__(self):
        return ExceptionLoadNote.message