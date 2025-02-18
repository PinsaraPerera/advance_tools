import os
from typing import Any, Dict, Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000")


class DBAPISearchToolInput(BaseModel):
    user_id: int = Field(..., title="User ID", description="The user ID to search for.")
    start_date: str = Field(..., title="Start Date", description="Start date (YYYY-MM-DD).")
    end_date: str = Field(..., title="End Date", description="End date (YYYY-MM-DD).")

class DBAPISearchTool(BaseTool):
    name: str = "Tool to retrieve user transactions from API call"
    description: str = "Retrieves user transactions filtered by date range from an API call."
    args_schema: Type[BaseModel] = DBAPISearchToolInput

    def _run(self, user_id: int, start_date: str, end_date: str) -> Dict[str, Any]:
        """Retrieve transactions based on user_id and date range from API."""
        url = f"{API_URL}/transactions/"
        
        params = {"user_id": user_id,"start_date": start_date, "end_date": end_date}

        try:
            # Make API call
            response = requests.post(url, json=params)
            response.raise_for_status()
            transactions = response.json()

            # Format results
            result = [
                {
                    "amount": tx["transaction_amount"],
                    "type": tx["transaction_type"],
                    "description": tx["transaction_description"],
                    "date": tx["transaction_date"],
                }
                for tx in transactions
            ]

            return {"success": True, "transactions": result}

        except requests.exceptions.RequestException as e:
            return {"success": False, "error": str(e)}
        

# uncomment the following lines to test the tool

# if __name__ == "__main__":
#     tool = DBAPISearchTool()

#     test_inputs = {
#         "user_id": 1,
#         "start_date": "2025-02-12",
#         "end_date": "2025-02-17",
#     }

#     result = tool._run(**test_inputs)
#     print("Test results:", result["transactions"])