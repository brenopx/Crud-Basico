# Import system libs
from pydantic import BaseModel

#######################################

class ProfessorCreate(BaseModel):
    nome : str
    cpf : int
    email : str
    endereco : str
    numero : int
    complemento : str
    estado : str

class Professor(ProfessorCreate):
    id_professor: int

    class Config:
        from_attributes = True
