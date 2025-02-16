from app.db.session import SessionLocal  # Make sure to import the session
from app.models.transaction_model import Transaction  # Import your Transaction model
from sqlalchemy.orm import Session

# Sample transactions to be inserted into the database
sample_transactions = [
    {"user_id": 1, "transaction_amount": 100.0, "transaction_type": "credit", "transaction_description": "Salary"},
    {"user_id": 1, "transaction_amount": -50.0, "transaction_type": "debit", "transaction_description": "Grocery Shopping"},
    {"user_id": 2, "transaction_amount": 200.0, "transaction_type": "credit", "transaction_description": "Freelance Payment"},
    {"user_id": 2, "transaction_amount": -20.0, "transaction_type": "debit", "transaction_description": "Coffee"},
    {"user_id": 3, "transaction_amount": 150.0, "transaction_type": "credit", "transaction_description": "Consulting Income"},
    {"user_id": 3, "transaction_amount": -30.0, "transaction_type": "debit", "transaction_description": "Restaurant"},
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
        print("✅ Sample data inserted successfully!")
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
