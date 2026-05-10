from appNotes.model.modelNotes import Notes,Level
import reflex as rx
from sqlmodel import *
from datetime import datetime
from ..component.toastNotes import toastNotes


class NotesStates(rx.State):
    note: str
    date: datetime
    notes: list[Notes] = []
    dictNotes: list[dict] = []
    level: int

    async def set_note(self, value:str ):
        self.note = value

    def set_level(self, value:str):
        if value == 'Alta':
            self.level = 1
        elif value == 'Media':
            self.level = 2
        elif value == 'Baja':
            self.level = 3

    def load_notes(self):
        with rx.session() as session:
            self.notes = session.exec(select(Notes).order_by(desc(Notes.date))).all()
            
            self.dictNotes = []
            for note in self.notes:
                self.dictNotes.append({
                    "id": note.id,
                    "note": note.note,
                    "date": note.date.strftime('%d'),  # Formateado
                    "level": note.level,
                    "user": note.user
                })
            

    def insertNotes(self):
        insNote = Notes(
            note=self.note,
            date=datetime.now(),
            level=self.level
        )

        with rx.session() as session:
            session.add(insNote)
            session.commit()

        self.note = ''
        # self.date = ''
        self.load_notes()
        self.level = 0
        
        return rx.toast(
                                "Nota Insertada!",
                                position="bottom-right",
                                style={
                                    "background-color": "green",
                                    "color": "white",
                                    "border": "1px solid green",
                                    "border-radius": "0.53m",
                                },
                            )
        
    def deleteNotes(self, id: int):
        with rx.session() as session:
            noteId = session.get(Notes, id)
            if noteId:
                session.delete(noteId)
                session.commit()
                self.load_notes()
        
        return rx.toast(
                                "Nota Eliminada!",
                                position="bottom-right",
                                style={
                                    "background-color": "red",
                                    "color": "white",
                                    "border": "1px solid red",
                                    "border-radius": "0.53m",
                                },
                            )