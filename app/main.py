from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine
from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


@app.get("/health")
async def root():
    return {"message": "the application is running"}


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/loans/", response_model=schemas.Loan)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    return crud.create_loan(db=db, loan=loan)


@app.get("/loans/{loan_id}", response_model=schemas.Loan)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = crud.get_loan(db, loan_id=loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.put("/loans/{loan_id}", response_model=schemas.Loan)
def update_loan(loan_id: int, loan: schemas.LoanUpdate, db: Session = Depends(get_db)):
    return crud.update_loan(db=db, loan_id=loan_id, loan=loan)


@app.delete("/loans/{loan_id}")
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    crud.delete_loan(db, loan_id=loan_id)
    return {"detail": "Loan deleted"}
