from typing import List
from pydantic import BaseModel, Field
from datetime import date

class Transaction(BaseModel):
    user_id: int
    transaction_amount: float
    transaction_type: str
    transaction_description: str
    transaction_date: date = Field(default_factory=date.today)

    class config:
        protected_namespace = ()

class TransactionInput(BaseModel):
    user_id: int
    start_date: date
    end_date: date

class TransactionOutput(BaseModel):
    transaction_amount: float
    transaction_type: str
    transaction_description: str
    transaction_date: date