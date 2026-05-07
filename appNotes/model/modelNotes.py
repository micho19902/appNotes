from sqlmodel import SQLModel, Field
import datetime


class Notes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: str
    note: str
    date: datetime.datetime
    level: int

class Level(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    level: str    