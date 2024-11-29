from sqlalchemy import Column, Integer, Float, String
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
    purpose = Column(String, nullable=False)


class MortgageLoan(Loan):
    __tablename__ = 'mortgage_loans'
    address = Column(String, nullable=False)
