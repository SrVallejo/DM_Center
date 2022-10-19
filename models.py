from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    Id: int
    Nombre: str
    Edad: int
    Notas: float
    Fecha: date