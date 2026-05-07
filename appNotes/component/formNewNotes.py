import reflex as rx
from ..model.modelNotes import Notes


def formNewNotes() -> rx.Component:
    return rx.box(
        rx.text(
            'Nota'
        ),
        rx.text_area(
            placeholder='Insertar Nota...',
            margin='20px'
        )
    )