from sqlalchemy.orm import Session
from app.models.transaction_model import Transaction
from app.schemas import transaction_schema
from datetime import date
from fastapi import HTTPException, status, Request
from typing import List


def get_transactions(db: Session, transaction: transaction_schema.TransactionInput):
    # Get the transactions between the start and end date
    transactions = db.query(Transaction).filter(
        Transaction.user_id == transaction.user_id,
        Transaction.transaction_date >= transaction.start_date,
        Transaction.transaction_date <= transaction.end_date
    ).all()

    # Return the transactions
    return [transaction_schema.TransactionOutput(
        transaction_amount=transaction.transaction_amount,
        transaction_type=transaction.transaction_type,
        transaction_description=transaction.transaction_description,
        transaction_date=transaction.transaction_date
    ) for transaction in transactions]