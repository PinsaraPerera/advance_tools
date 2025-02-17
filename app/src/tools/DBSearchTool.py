import os
from typing import Any, Dict, Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.models.transaction_model import Transaction
from datetime import datetime

class DBSearchToolInput(BaseModel):
    user_id: int = Field(..., title="User ID", description="The user ID to search for.")
    start_date: str = Field(..., title="Start Date", description="Start date (YYYY-MM-DD).")
    end_date: str = Field(..., title="End Date", description="End date (YYYY-MM-DD).")

class DBSearchTool(BaseTool):
    name: str = "Tool to retrieve user transactions from the database."
    description: str = "Retrieves user transactions filtered by date range."
    args_schema: Type[BaseModel] = DBSearchToolInput

    def _run(self, user_id: int, start_date: str, end_date: str) -> Dict[str, Any]:
        """Retrieve transactions based on user_id and date range."""
        db: Session = SessionLocal()

        try:
            # Convert date strings to actual date objects
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

            # Query transactions within the date range
            transactions = (
                db.query(Transaction)
                .filter(Transaction.user_id == user_id)
                .filter(Transaction.transaction_date >= start_date_obj)
                .filter(Transaction.transaction_date <= end_date_obj)
                .all()
            )

            # Format results
            result = [
                {
                    "amount": tx.transaction_amount,
                    "type": tx.transaction_type,
                    "description": tx.transaction_description,
                    "date": tx.transaction_date.strftime("%Y-%m-%d"),
                }
                for tx in transactions
            ]

            return {"success": True, "transactions": result}

        except Exception as e:
            return {"success": False, "error": str(e)}

        finally:
            db.close()

# uncomment the following lines to test the tool

# if __name__ == "__main__":
#     tool = DBSearchTool()

#     test_properties = {
#         "user_id": 1,
#         "start_date": "2025-02-12",
#         "end_date": "2025-02-17",
#     }

#     result = tool._run(user_id=test_properties["user_id"], start_date=test_properties["start_date"], end_date=test_properties["end_date"])
#     print("Test Result:", result["transactions"])
