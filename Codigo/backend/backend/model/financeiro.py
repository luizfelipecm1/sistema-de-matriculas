from model.usuario import Usuario
from model.aluno import Aluno
from pydantic import BaseModel

class Financeiro(BaseModel):
    valor : float
    data: str
    idAluno: Aluno
   

def cobrarMatricula(self):
    pass

    

