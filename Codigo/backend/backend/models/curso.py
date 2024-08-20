from models.disciplina import Disciplina
from pydantic import BaseModel


class Curso(BaseModel):
    nome: str
    creditos: int
    disciplinas: tuple[Disciplina]
