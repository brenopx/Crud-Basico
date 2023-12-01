# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Tcursoaluno

#######################################

# --------------------
def get_cursoaluno_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_cursoaluno = Tcursoaluno.get_cursoaluno_all(db)

    if (val_cursoaluno is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_cursoaluno)
# --------------------

# --------------------
def create_cursoaluno(new_cursoaluno:schemas.CursoAlunoCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_cursoaluno = Tcursoaluno.create_cursoaluno(db, new_cursoaluno)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_cursoaluno is None):
        m_name = f"cursoaluno data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_cursoaluno)
# --------------------

# --------------------
def update_cursoaluno_id_first(update_cursoaluno:schemas.CursoAluno, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    val_col = Tcursoaluno.update_cursoaluno_id_first(db, update_cursoaluno)

    if (val_col is None):
        m_name = f"cursoaluno data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_cursoaluno_id_first(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_cursoaluno = Tcursoaluno.delete_cursoaluno_id_first(db, id)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_cursoaluno is None):
        m_name = f"cursoaluno data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_cursoaluno)
# --------------------