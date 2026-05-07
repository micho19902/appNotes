from appNotes.model.modelNotes import Notes,Level
import reflex as rx
from sqlmodel import *
from datetime import datetime
from ..component.toastNotes import toastNotes


class NotesStates(rx.State):
    note: str
    date: datetime

    notes: list[Notes] = []

    async def set_note(self, value:str ):
        self.note = value


    def load_notes(self):
        with rx.session() as session:
            self.notes = session.exec(select(Notes)).all()
            print(self.notes)


    def insertNotes(self):
        insNote = Notes(
        note=self.note,
        date=datetime.now()
        )

        with rx.session() as session:
            session.add(insNote)
            session.commit()

        
        toastNotes()
        self.note = ''
        self.date = ''