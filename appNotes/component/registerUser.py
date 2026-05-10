import reflex as rx
from ..states.userStates import UserStates

def registerUser() -> rx.Component:
    return rx.center(
rx.card(
        rx.form(
        rx.vstack(
                rx.heading(
                    'Crear Cuenta'
                ),
                rx.divider(),
                rx.text('Username'),
                rx.input(
                    placeholder='Introduce un usuario',
                    on_change=UserStates.set_username,
                    value=UserStates.username
                ),
            
            # rx.hstack(
                rx.text('Email'),
                rx.input(
                    placeholder='Introduce un email',
                    value=UserStates.email,
                    on_change=UserStates.set_email,
                    type='email'
                ),
            
            # rx.hstack(
                rx.text('Password'),
                rx.input(
                    placeholder='Introduce un password',
                    value=UserStates.passw,
                    type='password',
                    on_change=UserStates.set_passw
                ),
            
            # rx.hstack(
                rx.text('Confirmar Password'),
                rx.input(
                    placeholder='Confirmar password',
                    value=UserStates.confirmPass,
                    type='password',
                    on_change=UserStates.set_cPass
                ),
                rx.divider(),
                rx.text(
                    UserStates.errorMsg
                ),
                rx.button('Crear', type='submit'),

                margin_bottom='20px',
            
        ),
        height='100%',
        on_submit=UserStates.insertUser,
        
        
    )
    )
    )
