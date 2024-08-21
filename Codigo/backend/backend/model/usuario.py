from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr


class Tipo(Enum):
    Aluno = "aluno"
    Professor = "professor"
    Secretario = "secretario"


class Usuario(BaseModel):
    nome: str
    tipo: Tipo
    email: EmailStr
    senha: str
    cpf: Optional[str] = None
