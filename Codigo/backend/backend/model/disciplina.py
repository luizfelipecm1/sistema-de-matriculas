from .aluno import Aluno
from .professor import Professor
from pydantic import BaseModel


class Disciplina(BaseModel):
    nome: str
    ativa: bool
    professor: Professor
    alunos: list[Aluno]
