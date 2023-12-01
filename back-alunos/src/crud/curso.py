# Import system libs
from sqlalchemy.orm import Session

# Import custom libs
from .. import models
from ..curso import schemas

class Tcurso:

    # --------------------
    def get_curso_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.curso).all()

        return(info)
    # --------------------

    # --------------------
    def get_curso_id_first(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.curso)

        info =  dbq.filter(models.curso.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_curso(db: Session, new_curso: schemas.CursoCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_curso = None
      
        db_curso = models.curso(
            nome = new_curso.nome,
            id_professor = new_curso.id_professor,
            id_aluno = new_curso.id_aluno
        )

        # Insert in database
        db.add(db_curso)
        db.commit()
        db.refresh(db_curso)
        
        return(db_curso)       
    # --------------------

    # --------------------
    def update_curso_id_first(db: Session, col_data: schemas.Curso):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_col = Tcurso.get_curso_id_first(db, col_data.id_professor)

        db_col.nome = col_data.nome
        db_col.id_professor = col_data.id_professor
        db_col.id_aluno = col_data.id_aluno

        db.commit()

        return (db_col)
    # --------------------

    # --------------------
    def delete_curso_professor_id_first(db: Session, id_professor: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Tcurso.get_curso_id_first(db, id_professor)

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
