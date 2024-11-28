from sqlalchemy import Column, Integer, Float
from .database import Base
# models.py


class Loan(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    term_months = Column(Integer, nullable=False)


class PersonalLoan(Loan):
    __tablename__ = 'personal_loans'
    # Additional fields specific to personal loans


class MortgageLoan(Loan):
    __tablename__ = 'mortgage_loans'
    # Additional fields specific to mortgage loans
