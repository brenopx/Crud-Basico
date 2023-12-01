# Import system libs
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import custom libs
from ..database import get_db
from . import schemas
from ..crud import Tprofessor

#######################################

# --------------------
def get_professor_all(db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''
    
    val_professor = Tprofessor.get_professor_all(db)

    if (val_professor is None):
        raise HTTPException(
            status_code=404, 
            detail=f"Error searching for available."
        )

    return(val_professor)
# --------------------

# --------------------
def create_professor(new_professor:schemas.ProfessorCreate, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_professor = Tprofessor.create_professor(db, new_professor)
    except Exception as exc:
        msg = f"Error {exc}"
        print(msg)
        raise HTTPException(status_code=520, detail=msg)

    if (db_professor is None):
        m_name = f"professor data"
        raise HTTPException(status_code=404, detail=f"Error creating {m_name}.")

    return(db_professor)
# --------------------

# --------------------
def update_professor(update_professor:schemas.Professor, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    val_col = Tprofessor.update_professor(db, update_professor)

    if (val_col is None):
        m_name = f"professor data"
        raise HTTPException(status_code=404, detail=f"Error updating {m_name}.")

    return(val_col)
# --------------------

# --------------------
def delete_professor(id: int, db:Session=Depends(get_db)):
    ''' Description \n
    `` (): \n
    return `` (): \n
    '''

    try:
        db_professor = Tprofessor.delete_professor(db, id)
    except Exception as exc:
        msg = f"Error {exc}"
        raise HTTPException(status_code=520, detail=msg)

    if (db_professor is None):
        m_name = f"professor data"
        raise HTTPException(status_code=404, detail=f"Error delete {m_name}.")

    return(db_professor)
# --------------------