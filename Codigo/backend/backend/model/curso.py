from model import Aluno
from .semestre import Semestre
from pydantic import BaseModel


class Curso(BaseModel):
    nome: str
    creditos: int
    semestres: list[Semestre]
    alunos: list[Aluno]
