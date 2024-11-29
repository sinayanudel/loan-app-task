from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models, schemas, crud

#note: normally we should we migrations
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# health api
@app.get("/health")
async def root():
    return {"message": "the application is running"}

# personal loans api
@app.post("/loans/personal", response_model=schemas.PersonalLoan)
def create_personal_loan(loan: schemas.PersonalLoanCreateUpdate, db: Session = Depends(get_db)):
    return crud.create_personal_loan(db=db, loan=loan)

@app.get("/loans/personal/{loan_id}", response_model=schemas.PersonalLoan)
def read_personal_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = crud.get_personal_loan(db, loan_id=loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.put("/loans/personal/{loan_id}", response_model=schemas.PersonalLoan)
def update_personal_loan(loan_id: int, loan: schemas.PersonalLoanCreateUpdate, db: Session = Depends(get_db)):
    return crud.update_personal_loan(db=db, loan_id=loan_id, loan=loan)


@app.delete("/loans/personal/{loan_id}")
def delete_personal_loan(loan_id: int, db: Session = Depends(get_db)):
    crud.delete_personal_loan(db, loan_id=loan_id)
    return {"detail": "Loan deleted"}

# mortgage loans api
