from app.db.session import SessionLocal 
from app.models.transaction_model import Transaction
from sqlalchemy.orm import Session
from datetime import date, timedelta

# Generate sample dates (past few days)
today = date.today()
dates = [today - timedelta(days=i) for i in range(6)]  # 6 different past dates

# Sample transactions with varying dates
sample_transactions = [
    {"user_id": 1, "transaction_amount": 100.0, "transaction_type": "credit", "transaction_description": "Salary", "transaction_date": dates[0]},
    {"user_id": 1, "transaction_amount": -50.0, "transaction_type": "debit", "transaction_description": "Grocery Shopping", "transaction_date": dates[1]},
    {"user_id": 2, "transaction_amount": 200.0, "transaction_type": "credit", "transaction_description": "Freelance Payment", "transaction_date": dates[2]},
    {"user_id": 2, "transaction_amount": -20.0, "transaction_type": "debit", "transaction_description": "Coffee", "transaction_date": dates[3]},
    {"user_id": 3, "transaction_amount": 150.0, "transaction_type": "credit", "transaction_description": "Consulting Income", "transaction_date": dates[4]},
    {"user_id": 3, "transaction_amount": -30.0, "transaction_type": "debit", "transaction_description": "Restaurant", "transaction_date": dates[5]},
]

# Function to insert sample data into the database
def insert_sample_data():
    # Create a session
    db: Session = SessionLocal()

    try:
        # Insert the sample transactions
        for transaction in sample_transactions:
            new_transaction = Transaction(**transaction)
            db.add(new_transaction)
        
        # Commit the transaction to the database
        db.commit()
        print("✅ Sample data inserted successfully with different dates!")
    except Exception as e:
        # If there's an error, rollback the transaction
        db.rollback()
        print(f"❌ Error inserting sample data: {e}")
    finally:
        # Close the session
        db.close()

# Call the function to insert the sample data
if __name__ == "__main__":
    insert_sample_data()
