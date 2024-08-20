from models import Curso
from models import Disciplina
from pydantic import BaseModel


class Semestre(BaseModel):
    periodo: int
    curso: Curso
    disciplinas: tuple[Disciplina]
