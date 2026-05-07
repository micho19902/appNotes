import reflex as rx
from rxconfig import config
from .model.modelNotes import Notes,Level

class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.heading(
            'Notes',
            width='auto|auto',
            size='9',
            align='center',
            color_scheme='amber',
            font_family='Comic Relief',
        ),
        # bg="#1A0126",
        width='auto|auto',
        padding='20px'
        # background="#702626"

    ),



app = rx.App(style={
    'background_color': "#110218"
    },
    stylesheets=[
        'https://fonts.googleapis.com/css2?family=Comic+Relief:wght@400;700&display=swap'

        ]
    
)
app.add_page(index)
