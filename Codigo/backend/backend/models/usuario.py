from typing import Optional
from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    cpf: Optional[str] = None