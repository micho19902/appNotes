import reflex as rx
from ..model.modelNotes import Notes
from ..states.notesStates import NotesStates


def formNewNotes() -> rx.Component:
    return rx.box(
        rx.text(
            'Nota'
        ),
        rx.text_area(
            placeholder='Insertar Nota...',
            value=NotesStates.note,
            margin='20px',
            on_change=NotesStates.set_note(NotesStates.note)
        )
    )