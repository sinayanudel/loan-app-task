from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
import os
import logging

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter()

logger = logging.getLogger(__name__)
security = HTTPBasic()


# Dependency to get the current user
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = os.getenv("BASIC_AUTH_USERNAME")
    correct_password = os.getenv("BASIC_AUTH_PASSWORD")
    if (
        credentials.username != correct_username
        or credentials.password != correct_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


# Mortgage loans API
@router.post("/", response_model=schemas.MortgageLoan)
def create_mortgage_loan(
    loan: schemas.MortgageLoanCreateUpdate,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user),
):
    logger.info(f"Creating mortgage loan with data: {loan}")
    return crud.create_loan(db=db, loan=loan, loan_model=models.MortgageLoan)


@router.get("/{loan_id}", response_model=schemas.MortgageLoan)
def read_mortgage_loan(
    loan_id: int,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user),
):
    if loan_id is None:
        raise HTTPException(status_code=400, detail="Loan ID must be provided")
    logger.info(f"Reading mortgage loan with ID: {loan_id}")
    db_loan = crud.get_loan(db, loan_id=loan_id, loan_model=models.MortgageLoan)
    if db_loan is None:
        logger.warning(f"Mortgage loan with ID {loan_id} not found")
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@router.put("/{loan_id}", response_model=schemas.MortgageLoan)
def update_mortgage_loan(
    loan_id: int,
    loan: schemas.MortgageLoanCreateUpdate,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user),
):
    if loan_id is None:
        raise HTTPException(status_code=400, detail="Loan ID must be provided")
    logger.info(f"Updating mortgage loan with ID: {loan_id} with data: {loan}")
    db_loan = crud.update_loan(
        db=db, loan_id=loan_id, loan=loan, loan_model=models.MortgageLoan
    )
    if db_loan is None:
        logger.warning(f"Mortgage loan with ID {loan_id} not found")
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@router.delete("/{loan_id}")
def delete_mortgage_loan(
    loan_id: int,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user),
):
    if loan_id is None:
        raise HTTPException(status_code=400, detail="Loan ID must be provided")
    logger.info(f"Deleting mortgage loan with ID: {loan_id}")
    crud.delete_loan(db, loan_id=loan_id, loan_model=models.MortgageLoan)
    return {"detail": "Loan deleted"}
