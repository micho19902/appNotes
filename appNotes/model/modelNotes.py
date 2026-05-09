from sqlmodel import SQLModel, Field
import datetime

class User(SQLModel, table=True):
    # __tablename__ = "users"
    
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True, max_length=50)
    email: str = Field(unique=True, index=True, max_length=100)
    hashed_password: str
    is_active: bool = True
    # created_at: datetime = Field(default_factory=datetime.now)
    # last_login: Optional[datetime] = None

class Notes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: int
    note: str
    date: datetime.datetime
    level: int

class Level(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    level: str    

