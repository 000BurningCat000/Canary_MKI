from database import db
from domain.notes.entities import Config
class NoteConfigDTO(db.Model):
    __table_name__ = "Note"
    id = db.Column(db.String(32),primary_key=True,auto_increment=False)
    file_ref = db.Column(db.String(120))
    signatures_ref = db.relationship("Signatures",backref="signatures",uselist=True)
    def toConfigEntity(self) -> Config:
        return Config(
            hash_file=self.id,
            old_hashes=self.signatures,
            file_ref=self.file_ref
        )
    @staticmethod
    def loadFromEntity(config:Config):
        return NoteConfigDTO(
            id=config.hash_file,
            file_ref=config.file_ref,
            signatures_ref=config.old_hashes
        )

        ...
class OldSignatureTable(db.Model):
    __table_name__ = "Signatures"
    id_signature = db.Column(db.Integer,primary_key=True)
    hash_value = db.Column(db.String(32))
    fk_registrer = db.Column(db.String(32),db.ForeignKey('Note.id'))


