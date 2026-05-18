import reflex as rx
from ..model.modelNotes import Notes
from ..states.notesStates import NotesStates


def cardNotes(notes: Notes, note: dict) -> rx.Component:
    # fecha = NotesStates.dictNotes.get('date','')
    return rx.cond(
        notes.level == 1,
        rx.box(
        rx.vstack(
            rx.text(
                
                notes.date
                # NotesStates.fechaForm
                # NotesStates.dictNotes[0]['date']
                # notes.id
            ),
            rx.divider(),
            rx.hstack(
            rx.text(
                notes.note
            ),
           
            rx.button(
                'Eliminar nota...',
                on_click=NotesStates.deleteNotes(notes.id),
                class_name='buttom'
                
            ),
            justify='between',
            width='100%',
            
            )
        ),
        class_name='cardNotes',
        background_color='red'
        ),
        rx.cond(
            notes.level == 2,
            rx.box(
            rx.vstack(
                rx.text(
                    notes.date
                    # NotesStates.dictNotes[0]['date']
                ),
                rx.divider(),
                rx.hstack(
                rx.text(
                    notes.note
                ),
            
                rx.button(
                    'Eliminar nota...',
                    on_click=NotesStates.deleteNotes(notes.id),
                    class_name='buttom'
                    
                ),
                justify='between',
                width='100%',
                
                )
            ),
            class_name='cardNotes',
            background_color='yellow',
            color='black'
            ),
            rx.cond(
                notes.level == 3,
                rx.box(
                rx.vstack(
                    rx.text(
                        notes.date
                        # NotesStates.dictNotes[0]['date']
                    ),
                    rx.divider(),
                    rx.hstack(
                    rx.text(
                        notes.note
                    ),
                
                    rx.button(
                        'Eliminar nota...',
                        on_click=NotesStates.deleteNotes(notes.id),
                        class_name='buttom'
                        
                    ),
                    justify='between',
                    width='100%',
                    
                    )
                ),
                class_name='cardNotes',
                background_color='green'
                ),
                rx.box(
                rx.vstack(
                    rx.text(
                        notes.date
                        # NotesStates.dictNotes[0]['date']
                    ),
                    rx.divider(),
                    rx.hstack(
                    rx.text(
                        notes.note
                    ),
                
                    rx.button(
                        'Eliminar nota...',
                        on_click=NotesStates.deleteNotes(notes.id),
                        class_name='buttom'
                        
                    ),
                    justify='between',
                    width='100%',
                    
                    )
                ),
                class_name='cardNotes',
                # background_color='green'
                )
                
            )      
        
        )      
    )      