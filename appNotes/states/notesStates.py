from appNotes.model.modelNotes import Notes,Level
import reflex as rx
from sqlmodel import *
from datetime import datetime


class NotesStates(rx.State):
  pass