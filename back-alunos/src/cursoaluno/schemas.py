# Import system libs
from pydantic import BaseModel

#######################################

class CursoAlunoCreate(BaseModel):
    id_aluno : int
    id_curso : int

class CursoAluno(CursoAlunoCreate):
    class Config:
        from_attributes = True
