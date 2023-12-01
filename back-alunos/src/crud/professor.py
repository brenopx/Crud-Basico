# Import system libs
from sqlalchemy.orm import Session

# Import custom libs
from .. import models
from ..professor import schemas

class Tprofessor:

    # --------------------
    def get_professor_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.professor).all()

        return(info)
    # --------------------

    # --------------------
    def get_professor_id(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.professor)

        info =  dbq.filter(models.professor.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_professor(db: Session, new_professor: schemas.professorCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_professor = None
      
        db_professor = models.professor(
            nome = new_professor.nome,
            cpf = new_professor.cpf,
            email = new_professor.email,
            endereco = new_professor.endereco,
            numero = new_professor.numero,
            complemento = new_professor.complemento,
            estado = new_professor.estado
        )

        # Insert in database
        db.add(db_professor)
        db.commit()
        db.refresh(db_professor)
        
        return(db_professor)       
    # --------------------

    # --------------------
    def update_professor(db: Session, col_data: schemas.professor):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        db_col = Tprofessor.get_professor_id(db, col_data.id_professor)

        db_col.id_professor = col_data.id_professor
        db_col.nome = col_data.nome
        db_col.cpf = col_data.cpf
        db_col.email = col_data.email
        db_col.endereco = col_data.endereco
        db_col.numero = col_data.numero
        db_col.complemento = col_data.complemento
        db_col.estado = col_data.estado

        db.commit()

        return (db_col)
    # --------------------

    # --------------------
    def delete_professor(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Tprofessor.get_professor_id(db, id)

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
