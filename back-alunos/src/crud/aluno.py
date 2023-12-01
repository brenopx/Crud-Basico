# Import system libs
from sqlalchemy.orm import Session

# Import custom libs
from .. import models
from ..aluno import schemas

class Taluno:

    # --------------------
    def get_aluno_all(db: Session):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        info = db.query(models.Aluno).all()

        return(info)
    # --------------------

    # --------------------
    def get_aluno_id(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        # Declare the query
        dbq = db.query(models.Aluno)

        info =  dbq.filter(models.Aluno.id == id).first()

        return(info)
    # --------------------

    # --------------------
    def create_aluno(db: Session, new_aluno: schemas.AlunoCreate):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        db_aluno = None
      
        db_aluno = models.Aluno(
            nome = new_aluno.nome,
            cpf = new_aluno.cpf,
            email = new_aluno.email,
            endereco = new_aluno.endereco,
            numero = new_aluno.numero,
            complemento = new_aluno.complemento,
            estado = new_aluno.estado
        )

        # Insert in database
        db.add(db_aluno)
        db.commit()
        db.refresh(db_aluno)
        
        return(db_aluno)       
    # --------------------

    # --------------------
    def update_aluno(db: Session, col_data: schemas.Aluno):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        db_col = Taluno.get_aluno_id(db, col_data.id_aluno)

        db_col.id_aluno = col_data.id_aluno
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
    def delete_aluno(db: Session, id: int):
        ''' Description \n
        `` (): \n
        return `` (): \n
        '''
        
        # Declare the query
        ds = Taluno.get_aluno_id(db, id)

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
