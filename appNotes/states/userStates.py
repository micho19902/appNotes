from ..model.modelNotes import User
import reflex as rx
from ..utils.security import hash_password,verify_password
from sqlmodel import select



class UserStates(rx.State):
    username: str
    email: str
    passw: str
    confirmPass: str
    errorMsg: str


    async def set_username(self, value: str):
        self.username = value
        self.errorMsg = ''

    def set_email(self, value: str):
        self.email = value
        self.errorMsg = ''

    def set_passw(self, value: str):
        self.passw = value
        self.errorMsg = ''

    def set_cPass(self, value: str):
        self.confirmPass = value
        self.errorMsg = ''





    def insertUser(self):
        
        if not self.username or not self.email or not self.passw:
            self.errorMsg = "❌ Todos los campos son requeridos"
            return

        if self.passw != self.confirmPass:
            self.errorMsg = '❌ Las contraseñas no coinciden'
            return

        insUser = User(
            username = self.username,
            email = self.email,
            hashed_password= hash_password(self.passw)
        )

        with rx.session() as session:
            existUser = session.exec(select(User).where(User.username == self.username)).first()
            existEmail = session.exec(select(User).where(User.email == self.email)).first()

            if existUser:
                self.errorMsg = '❌ El usuario ya existe'
                return
            
            if existEmail:
                self.errorMsg = '❌ El email ya esta en uso'
                return


            session.add(insUser)
            session.commit()

        self.username = ''
        self.email = ''
        self.passw = ''
        self.confirmPass = ''
        
        return rx.redirect('/')
        # return rx.toast(
        #                         "Usuario Creado!",
        #                         position="bottom-right",
        #                         style={
        #                             "background-color": "green",
        #                             "color": "white",
        #                             "border": "1px solid green",
        #                             "border-radius": "0.53m",
        #                         },
        #                     )
    

