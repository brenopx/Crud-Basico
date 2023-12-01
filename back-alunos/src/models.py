from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Aluno(Base):
    __tablename__ = "aluno"

    id_aluno = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(Integer)
    email = Column(String)
    endereco = Column(String)
    numero = Column(Integer)
    complemento = Column(String)
    estado = Column(String)

    # Other tables
    cursoaluno = relationship("CursoAluno", back_populates="aluno")

class Professor(Base):
    __tablename__ = "professor"

    id_professor = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(Integer)
    email = Column(String)
    endereco = Column(String)
    numero = Column(Integer)
    complemento = Column(String)
    estado = Column(String)

    # Other tables
    curso = relationship("Curso", back_populates="professor")

class Curso(Base):
    __tablename__ = "curso"

    id_curso = Column(Integer, primary_key=True, index=True)
    nome = Column(String)

    # Other tables
    professor = relationship("Professor", back_populates="curso")
    id_professor = Column(Integer, ForeignKey("professor.id_professor"))


class CursoAluno(Base):
    __tablename__ = "cursoaluno"

    # Other tables
    aluno = relationship("Aluno", back_populates="cursoaluno")
    id_aluno = Column(Integer, ForeignKey("aluno.id_aluno"))

    curso = relationship("Curso", back_populates="cursoaluno")
    id_curso = Column(Integer, ForeignKey("curso.id_curso"))

