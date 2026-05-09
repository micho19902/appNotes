import reflex as rx
from rxconfig import config
from .model.modelNotes import Notes,Level
from appNotes.component.formNewNotes import formNewNotes
from datetime import datetime
from .component.toastNotes import toastNotes
from .states.notesStates import *
from .component.cardNotes import cardNotes
# from .component.regiterUser import register_page
# from .component.login import login_page





# class State(rx.State):
#     """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.hstack(
            rx.heading(
                'Notes',
                width='auto|auto',
                size='9',
                align='left',
                color_scheme='amber',
                font_family='Comic Relief',
                sticky='left',
                margin='20px'
            ),
            rx.hstack(
                rx.color_mode.button(position='rigt'),

                rx.dialog.root(
                    rx.dialog.trigger(rx.button(
                        rx.icon(tag='plus'),
                        class_name='buttom'
                        ), ),
                    rx.dialog.content(
                        rx.dialog.title("Insertar nueva Nota"),
                        rx.dialog.description(
                            
                            formNewNotes()
                        ),
                        rx.dialog.close(
                            rx.button("Insertar Nota", size="3", class_name='buttom', on_click=NotesStates.insertNotes
                            ),
                        ),
                    ),
                ),
                rx.dialog.root(
                    rx.dialog.trigger(rx.button(
                        rx.icon(tag='user'),
                        class_name='buttom'
                        ), ),
                    rx.dialog.content(
                        # rx.dialog.title("Registrar nuevo Usuarios"),
                        rx.dialog.description(
                            
                            # login_page()
                        ),
                        # rx.dialog.close(
                        #     rx.button("Crear", size="3", class_name='buttom', on_click=NotesStates.insertNotes
                        #     ),
                        # ),
                    ),
                ),
                # margin='20px',
                
            ),
            justify='between',
            width='100%',
            align='center'
        ),
        rx.divider(),
        rx.box(
            rx.box(
                rx.foreach(
                    NotesStates.notes,
                    cardNotes,

                )
            ),
            
        ),
        # bg="#1A0126",
        # width='100px|auto',
        padding='20px',
        # background="#702626"

    ),



app = rx.App(style={
    # 'background_color': "#110218"
    },
    stylesheets=[
        'https://fonts.googleapis.com/css2?family=Comic+Relief:wght@400;700&display=swap',
        './styles/styles.css'

        ]
    
)
# app.add_page(register_page, route='/register')
# app.add_page(login_page, route='/login')
app.add_page(index, on_load=NotesStates.load_notes)
