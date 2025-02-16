from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    transaction_amount = Column(Float, nullable=False)
    transaction_type = Column(String, nullable=False)  # "credit" or "debit"
    transaction_description = Column(String, nullable=True)
