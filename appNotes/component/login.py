import reflex as rx
from ..model.modelNotes import User



def loginUser() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.heading('Login'),
                rx.divider(),
                rx.text(
                    'Username'
                ),
                rx.input(
                    placeholder='Username'
                ),
                rx.text('Password'),
                rx.input(
                    placeholder='Introduce el password'
                ),
                rx.divider(),
                rx.hstack(
                rx.text(
                    'Eres nuevo?'
                ),
                rx.link(
                    'Registrate aqui', href='/register'
                )
                ),

                margin_bottom='20px'
            )
    )



