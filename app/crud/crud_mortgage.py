from sqlalchemy.orm import Session
from app import models, schemas


def get_loan(db: Session, loan_id: int):
    return (
        db.query(models.MortgageLoan).filter(models.MortgageLoan.id == loan_id).first()
    )


def create_loan(db: Session, loan: schemas.MortgageLoanCreateUpdate):
    db_loan = models.MortgageLoan(**loan.dict())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def update_loan(db: Session, loan_id: int, loan: schemas.MortgageLoanCreateUpdate):
    db_loan = get_loan(db, loan_id)
    if db_loan is None:
        return None
    for key, value in loan.dict().items():
        setattr(db_loan, key, value)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def delete_loan(db: Session, loan_id: int):
    db_loan = get_loan(db, loan_id)
    if db_loan:
        db.delete(db_loan)
        db.commit()
