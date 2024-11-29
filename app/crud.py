from sqlalchemy.orm import Session
from . import models, schemas

# personal loans CRUD
def get_personal_loan(db: Session, loan_id: int):
    return db.query(models.PersonalLoan).filter(models.PersonalLoan.id == loan_id).first()


def create_personal_loan(db: Session, loan: schemas.PersonalLoanCreateUpdate):
    db_loan = models.PersonalLoan(**loan.dict())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def update_personal_loan(db: Session, loan_id: int, loan: schemas.PersonalLoanCreateUpdate):
    db_loan = get_loan(db, loan_id)
    if db_loan:
        for key, value in loan.dict().items():
            setattr(db_loan, key, value)
        db.commit()
        db.refresh(db_loan)
    return db_loan


def delete_personal_loan(db: Session, loan_id: int):
    db_loan = get_loan(db, loan_id)
    if db_loan:
        db.delete(db_loan)
        db.commit()

# Mortgage loans CRUD
