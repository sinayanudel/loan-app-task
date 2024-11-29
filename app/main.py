from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models, schemas, crud

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
    return crud.create_loan(db=db, loan=loan, loan_model=models.PersonalLoan)


@app.get("/loans/personal/{loan_id}", response_model=schemas.PersonalLoan)
def read_personal_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = crud.get_loan(db, loan_id=loan_id, loan_model=models.PersonalLoan)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.put("/loans/personal/{loan_id}", response_model=schemas.PersonalLoan)
def update_personal_loan(
    loan_id: int, loan: schemas.PersonalLoanCreateUpdate, db: Session = Depends(get_db)
):
    db_loan = crud.update_loan(
        db=db, loan_id=loan_id, loan=loan, loan_model=models.PersonalLoan
    )
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.delete("/loans/personal/{loan_id}")
def delete_personal_loan(loan_id: int, db: Session = Depends(get_db)):
    crud.delete_loan(db, loan_id=loan_id, loan_model=models.PersonalLoan)
    return {"detail": "Loan deleted"}


# Mortgage loans API
@app.post("/loans/mortgage", response_model=schemas.MortgageLoan)
def create_mortgage_loan(
    loan: schemas.MortgageLoanCreateUpdate, db: Session = Depends(get_db)
):
    return crud.create_loan(db=db, loan=loan, loan_model=models.MortgageLoan)


@app.get("/loans/mortgage/{loan_id}", response_model=schemas.MortgageLoan)
def read_mortgage_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = crud.get_loan(db, loan_id=loan_id, loan_model=models.MortgageLoan)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.put("/loans/mortgage/{loan_id}", response_model=schemas.MortgageLoan)
def update_mortgage_loan(
    loan_id: int, loan: schemas.MortgageLoanCreateUpdate, db: Session = Depends(get_db)
):
    db_loan = crud.update_loan(
        db=db, loan_id=loan_id, loan=loan, loan_model=models.MortgageLoan
    )
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.delete("/loans/mortgage/{loan_id}")
def delete_mortgage_loan(loan_id: int, db: Session = Depends(get_db)):
    crud.delete_loan(db, loan_id=loan_id, loan_model=models.MortgageLoan)
    return {"detail": "Loan deleted"}
