import reflex as rx

def toastNotes() -> rx.Component:
    return rx.toast(
                                "Nota Insertada!",
                                position="top-right",
                                style={
                                    "background-color": "green",
                                    "color": "white",
                                    "border": "1px solid green",
                                    "border-radius": "0.53m",
                                },
                            ),