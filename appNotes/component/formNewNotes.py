import reflex as rx
from ..model.modelNotes import Notes
from ..states.notesStates import NotesStates
from datetime import datetime


def formNewNotes() -> rx.Component:
    fecha = datetime.now()
    return rx.box(
        rx.text(
            'Nota'
        ),
        rx.text_area(
            placeholder='Insertar Nota...',
            value=NotesStates.note,
            margin='20px',
            on_change=NotesStates.set_note
        ),
        rx.hstack(
            rx.text('Fecha'),
            rx.select(['Alta', 'Media', 'Baja', '-'], placeholder='Seleccionar nivel de importancia...',
                      on_change=NotesStates.set_level),
            print(fecha)
        )
    )