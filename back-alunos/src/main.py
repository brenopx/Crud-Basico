from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

# Import custom libs
from . import database
from .database import engine

from .aluno import routes as aluno_routes
from .aluno import schemas as aluno_schemas

from .professor import routes as professor_routes
from .professor import schemas as professor_schemas

from .curso import routes as curso_routes
from .curso import schemas as curso_schemas

from .cursoaluno import routes as cursoaluno_routes
from .cursoaluno import schemas as cursoaluno_schemas

database.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Application Routes

### aluno
app.add_api_route("/create_aluno",
    methods=["POST"], 
    response_model=aluno_schemas.Aluno,
    endpoint=aluno_routes.create_aluno)

app.add_api_route("/get_aluno_all",
    methods=["GET"], 
    response_model=List[aluno_schemas.Aluno],
    endpoint=aluno_routes.get_aluno_all)

app.add_api_route("/update_aluno",
    methods=["PUT"], 
    response_model=aluno_schemas.Aluno,
    endpoint=aluno_routes.update_aluno)

app.add_api_route("/delete_aluno/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=aluno_routes.delete_aluno)

### professor
app.add_api_route("/create_professor",
    methods=["POST"], 
    response_model=professor_schemas.Professor,
    endpoint=professor_routes.create_professor)

app.add_api_route("/get_professor_all",
    methods=["GET"], 
    response_model=List[professor_schemas.Professor],
    endpoint=professor_routes.get_professor_all)

app.add_api_route("/update_professor",
    methods=["PUT"], 
    response_model=professor_schemas.Professor,
    endpoint=professor_routes.update_professor)

app.add_api_route("/delete_professor/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=professor_routes.delete_professor)

### curso
app.add_api_route("/create_curso",
    methods=["POST"], 
    response_model=curso_schemas.Curso,
    endpoint=curso_routes.create_curso)

app.add_api_route("/get_curso_all",
    methods=["GET"], 
    response_model=List[curso_schemas.Curso],
    endpoint=curso_routes.get_curso_all)

app.add_api_route("/update_curso_id_first",
    methods=["PUT"], 
    response_model=curso_schemas.Curso,
    endpoint=curso_routes.update_curso_id_first)

app.add_api_route("/delete_curso_professor_id_first/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=curso_routes.delete_curso_professor_id_first)

### cursoaluno
app.add_api_route("/create_cursoaluno",
    methods=["POST"], 
    response_model=cursoaluno_schemas.CursoAluno,
    endpoint=cursoaluno_routes.create_cursoaluno)

app.add_api_route("/get_cursoaluno_all",
    methods=["GET"], 
    response_model=List[cursoaluno_schemas.CursoAluno],
    endpoint=cursoaluno_routes.get_cursoaluno_all)

app.add_api_route("/update_cursoaluno_id_first",
    methods=["PUT"], 
    response_model=cursoaluno_schemas.CursoAluno,
    endpoint=cursoaluno_routes.update_cursoaluno_id_first)

app.add_api_route("/delete_cursoaluno_id_first/{id}",
    methods=["DELETE"], 
    response_model=bool,
    endpoint=cursoaluno_routes.delete_cursoaluno_id_first)
