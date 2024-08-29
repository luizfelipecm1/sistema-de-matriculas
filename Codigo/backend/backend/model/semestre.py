from .disciplina import Disciplina
from pydantic import BaseModel


class Semestre(BaseModel):
    periodo: int
    disciplinas: list[Disciplina]