from pydantic import BaseModel
from typing import Optional


class LoanBase(BaseModel):
    amount: float
    interest_rate: float
    term_months: int


class LoanCreate(LoanBase):
    pass


class LoanUpdate(LoanBase):
    pass


class Loan(LoanBase):
    id: int

    class Config:
        orm_mode = True
