from pydantic import BaseModel
from typing import Optional


class LoanBase(BaseModel):
    amount: float
    interest_rate: float
    term_months: int


class PersonalLoanBase(LoanBase):
    purpose: str
    

class MortgageLoanBase(LoanBase):
    address: str

class PersonalLoanCreateUpdate(PersonalLoanBase):
    pass

class MortgageLoanCreateUpdate(MortgageLoanBase):
    pass

class PersonalLoan(PersonalLoanBase):
    id: int

class MortgageLoan(MortgageLoanBase):
    id: int

    class Config:
        orm_mode = True
