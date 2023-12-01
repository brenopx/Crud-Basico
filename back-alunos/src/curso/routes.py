# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Tcurso

#######################################

# --------------------
def get_curso_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_curso = Tcurso.get_curso_all(db)

    if (val_curso is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_curso)
# --------------------

# --------------------
def create_curso(new_curso:schemas.CursoCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_curso = Tcurso.create_curso(db, new_curso)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_curso is None):
        m_name = f"curso data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_curso)
# --------------------

# --------------------
def update_curso_id_first(update_curso:schemas.Curso, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    val_col = Tcurso.update_curso_id_first(db, update_curso)

    if (val_col is None):
        m_name = f"curso data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_curso_professor_id_first(id_professor: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_curso = Tcurso.delete_curso_professor_id_first(db, id_professor)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_curso is None):
        m_name = f"curso data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_curso)
# --------------------