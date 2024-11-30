import logging
import ssl
import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

from .database import engine, get_db
from . import models, schemas, crud

# Note: Normally we should use migrations
models.Base.metadata.create_all(bind=engine)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add HTTPS redirect middleware only in production
if os.getenv("ENV") == "production":
    app.add_middleware(HTTPSRedirectMiddleware)


# Middleware to log requests
@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response


# Health API
@app.get("/health")
async def root():
    logger.info("Health check endpoint called")
    return {"message": "the application is running"}


# Personal loans API
@app.post("/loans/personal", response_model=schemas.PersonalLoan)
def create_personal_loan(
    loan: schemas.PersonalLoanCreateUpdate, db: Session = Depends(get_db)
):
    logger.info(f"Creating personal loan with data: {loan}")
    return crud.create_loan(db=db, loan=loan, loan_model=models.PersonalLoan)


@app.get("/loans/personal/{loan_id}", response_model=schemas.PersonalLoan)
def read_personal_loan(loan_id: int, db: Session = Depends(get_db)):
    logger.info(f"Reading personal loan with ID: {loan_id}")
    db_loan = crud.get_loan(db, loan_id=loan_id, loan_model=models.PersonalLoan)
    if db_loan is None:
        logger.warning(f"Personal loan with ID {loan_id} not found")
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.put("/loans/personal/{loan_id}", response_model=schemas.PersonalLoan)
def update_personal_loan(
    loan_id: int, loan: schemas.PersonalLoanCreateUpdate, db: Session = Depends(get_db)
):
    logger.info(f"Updating personal loan with ID: {loan_id} with data: {loan}")
    db_loan = crud.update_loan(
        db=db, loan_id=loan_id, loan=loan, loan_model=models.PersonalLoan
    )
    if db_loan is None:
        logger.warning(f"Personal loan with ID {loan_id} not found")
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.delete("/loans/personal/{loan_id}")
def delete_personal_loan(loan_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting personal loan with ID: {loan_id}")
    crud.delete_loan(db, loan_id=loan_id, loan_model=models.PersonalLoan)
    return {"detail": "Loan deleted"}


# Mortgage loans API
@app.post("/loans/mortgage", response_model=schemas.MortgageLoan)
def create_mortgage_loan(
    loan: schemas.MortgageLoanCreateUpdate, db: Session = Depends(get_db)
):
    logger.info(f"Creating mortgage loan with data: {loan}")
    return crud.create_loan(db=db, loan=loan, loan_model=models.MortgageLoan)


@app.get("/loans/mortgage/{loan_id}", response_model=schemas.MortgageLoan)
def read_mortgage_loan(loan_id: int, db: Session = Depends(get_db)):
    logger.info(f"Reading mortgage loan with ID: {loan_id}")
    db_loan = crud.get_loan(db, loan_id=loan_id, loan_model=models.MortgageLoan)
    if db_loan is None:
        logger.warning(f"Mortgage loan with ID {loan_id} not found")
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.put("/loans/mortgage/{loan_id}", response_model=schemas.MortgageLoan)
def update_mortgage_loan(
    loan_id: int, loan: schemas.MortgageLoanCreateUpdate, db: Session = Depends(get_db)
):
    logger.info(f"Updating mortgage loan with ID: {loan_id} with data: {loan}")
    db_loan = crud.update_loan(
        db=db, loan_id=loan_id, loan=loan, loan_model=models.MortgageLoan
    )
    if db_loan is None:
        logger.warning(f"Mortgage loan with ID {loan_id} not found")
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@app.delete("/loans/mortgage/{loan_id}")
def delete_mortgage_loan(loan_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting mortgage loan with ID: {loan_id}")
    crud.delete_loan(db, loan_id=loan_id, loan_model=models.MortgageLoan)
    return {"detail": "Loan deleted"}


if __name__ == "__main__":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain("c:/cert.pem", keyfile="c:/key.pem")
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_context=ssl_context)
