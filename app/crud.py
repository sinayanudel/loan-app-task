from sqlalchemy.orm import Session
from app import models, schemas


def get_loan(db: Session, loan_id: int, loan_model):
    return db.query(loan_model).filter(loan_model.id == loan_id).first()


def create_loan(db: Session, loan: schemas.LoanBase, loan_model):
    db_loan = loan_model(**loan.dict())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def update_loan(db: Session, loan_id: int, loan: schemas.LoanBase, loan_model):
    db_loan = get_loan(db, loan_id, loan_model)
    if db_loan is None:
        return None
    for key, value in loan.dict().items():
        setattr(db_loan, key, value)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def delete_loan(db: Session, loan_id: int, loan_model):
    db_loan = get_loan(db, loan_id, loan_model)
    if db_loan:
        db.delete(db_loan)
        db.commit()
