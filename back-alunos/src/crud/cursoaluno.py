# Import system libs
from sqlalchemy.orm import Session

# Import custom libs
from .. import models
from ..cursoaluno import schemas


class Tcursoaluno:

    # --------------------
    def get_cursoaluno_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.CursoAluno).all()

        return(info)
    # --------------------

    # --------------------
    def get_cursoaluno_id_first(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.CursoAluno)

        info =  dbq.filter(models.CursoAluno.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_cursoaluno(db: Session, new_cursoaluno: schemas.CursoAlunoCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_cursoaluno = None
      
        db_cursoaluno = models.cursoaluno(
            id_aluno = new_cursoaluno.id_aluno,
            id_curso = new_cursoaluno.id_curso
        )

        # Insert in database
        db.add(db_cursoaluno)
        db.commit()
        db.refresh(db_cursoaluno)
        
        return(db_cursoaluno)       
    # --------------------

    # --------------------
    def update_cursoaluno_id_first(db: Session, col_data: schemas.CursoAluno):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        db_col = Tcursoaluno.get_cursoaluno_id_first(db, col_data.id_aluno)

        db_col.id_aluno : col_data.id_aluno
        db_col.id_curso : col_data.id_curso

        db.commit()

        return (db_col)
    # --------------------

    # --------------------
    def delete_cursoaluno_id_first(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Tcursoaluno.get_cursoaluno_id_first(db, id)

        if (ds is not None):
            # Remove from database
            db.delete(ds)
            db.commit()
            # Parse data
            ds_answer = True
        else:
            ds_answer = False
        
        return (ds_answer)
    # --------------------