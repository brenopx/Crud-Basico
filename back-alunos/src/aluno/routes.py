# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Taluno

#######################################

# --------------------
def get_aluno_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_aluno = Taluno.get_aluno_all(db)

    if (val_aluno is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_aluno)
# --------------------

# --------------------
def create_aluno(new_aluno:schemas.alunoCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_aluno = Taluno.create_aluno(db, new_aluno)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_aluno is None):
        m_name = f"aluno data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_aluno)
# --------------------

# --------------------
def update_aluno(update_aluno:schemas.aluno, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    val_col = Taluno.update_aluno(db, update_aluno)

    if (val_col is None):
        m_name = f"aluno data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_aluno(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_aluno = Taluno.delete_aluno(db, id)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_aluno is None):
        m_name = f"aluno data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_aluno)
# --------------------