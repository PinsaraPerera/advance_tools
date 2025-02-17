from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import transaction_schema
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.crud.transaction as transaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=List[transaction_schema.TransactionOutput])
def create_transaction(transaction_data: transaction_schema.TransactionInput, db: Session = Depends(get_db)):
    return transaction.get_transactions(db=db, transaction=transaction_data)