from Codigo.backend.backend.model.curso import Curso
from model.aluno import Aluno
from pydantic import BaseModel

class Financeiro(BaseModel):
    valor : float
    data: str
    idAluno: Aluno
    curso: Curso

def cobrarMatricula(self):
    pass

    

