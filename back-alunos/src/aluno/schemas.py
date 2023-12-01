# Import system libs
from pydantic import BaseModel

#######################################

class AlunoCreate(BaseModel):
    nome : str
    cpf : int
    email : str
    endereco : str
    numero : int
    complemento : str
    estado : str

class Aluno(AlunoCreate):
    id_aluno: int

    class Config:
        from_attributes = True
