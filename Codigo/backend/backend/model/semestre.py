from model import Curso
from model import Disciplina
from pydantic import BaseModel


class Semestre(BaseModel):
    periodo: int
    curso: Curso
    disciplinas: tuple[Disciplina]
