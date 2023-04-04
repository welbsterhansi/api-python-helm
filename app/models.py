from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    nome: str
    cpf: int
    chip: int