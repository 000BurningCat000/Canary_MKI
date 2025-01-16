class ExceptionLoadNote(Exception):
    message:str = 'Note cant be loaded!'
    def __str__(self):
        return ExceptionLoadNote.message

    