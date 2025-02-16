from app.db.base import Base
from app.db.session import engine
from app.models.transaction_model import Transaction

# Create all tables in the database
try:
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")
