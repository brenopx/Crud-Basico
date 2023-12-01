# Import system libs
from pydantic import BaseModel

#######################################

class CursoCreate(BaseModel):
    nome : str
    id_professor : int
    id_aluno: int

class Curso(CursoCreate):
    class Config:
        from_attributes = True
