from model.aluno import Aluno
from pydantic import BaseModel


class Matricula(BaseModel):
    idMatricula: int
    data: str
    aluno: Aluno
    
