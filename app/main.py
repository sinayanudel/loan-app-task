from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models, schemas
from .crud import crud_personal, crud_mortgage

# Note: Normally we should use migrations
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Health API
@app.get("/health")
async def root():
    return {"message": "the application is running"}


# Personal loans API
@app.post("/loans/personal", response_model=schemas.PersonalLoan)
def create_personal_loan(
    loan: schemas.PersonalLoanCreateUpdate, db: Session = Depends(get_db)
):
    return crud_personal.create_loan(db=db, loan=loan)


@app.get("/loans/personal/{loan_id}", response_model=schemas.PersonalLoan)
def read_personal_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = crud_personal.get_loan(db, loan_id=loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.put("/loans/personal/{loan_id}", response_model=schemas.PersonalLoan)
def update_personal_loan(
    loan_id: int, loan: schemas.PersonalLoanCreateUpdate, db: Session = Depends(get_db)
):
    return crud_personal.update_loan(db=db, loan_id=loan_id, loan=loan)


@app.delete("/loans/personal/{loan_id}")
def delete_personal_loan(loan_id: int, db: Session = Depends(get_db)):
    crud_personal.delete_loan(db, loan_id=loan_id)
    return {"detail": "Loan deleted"}


# Mortgage loans API
@app.post("/loans/mortgage", response_model=schemas.MortgageLoan)
def create_mortgage_loan(
    loan: schemas.MortgageLoanCreateUpdate, db: Session = Depends(get_db)
):
    return crud_mortgage.create_loan(db=db, loan=loan)


@app.get("/loans/mortgage/{loan_id}", response_model=schemas.MortgageLoan)
def read_mortgage_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = crud_mortgage.get_loan(db, loan_id=loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.put("/loans/mortgage/{loan_id}", response_model=schemas.MortgageLoan)
def update_mortgage_loan(
    loan_id: int, loan: schemas.MortgageLoanCreateUpdate, db: Session = Depends(get_db)
):
    return crud_mortgage.update_loan(db=db, loan_id=loan_id, loan=loan)


@app.delete("/loans/mortgage/{loan_id}")
def delete_mortgage_loan(loan_id: int, db: Session = Depends(get_db)):
    crud_mortgage.delete_loan(db, loan_id=loan_id)
    return {"detail": "Loan deleted"}
