import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd

# Define the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure the logs directory exists at the project root
log_dir = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
log_file = os.path.join(log_dir, "database_setup.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("🚀 Database Setup Log initialized successfully!")

# Load environment variables
load_dotenv("../.env")

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")


def get_db_connection():
    """Create and return database engine."""
    try:
        DATABASE_URL = (
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))  # Test connection
        logging.info("✅ Successfully connected to the PostgreSQL database.")
        return engine
    except Exception as e:
        logging.error(f"❌ Database connection failed: {e}")
        raise


def create_table(engine):
    """Create Medical_DataWarehouse table if it does not exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Medical_DataWarehouse (
        id SERIAL PRIMARY KEY,
        channel_name TEXT,
        channel_title TEXT,
        message TEXT,
        text_date TIMESTAMP,
        emoji_used TEXT
    );
    """
    try:
        with engine.connect().execution_options(
            isolation_level="AUTOCOMMIT"
        ) as connection:
            connection.execute(text(create_table_query))
        logging.info("✅ Table 'Medical_DataWarehouse' created successfully.")
    except Exception as e:
        logging.error(f"❌ Error creating table: {e}")
        raise


def insert_data(engine, cleaned_df):
    """Inserts cleaned Telegram data into PostgreSQL database."""
    try:
        # Convert NaT timestamps to None (NULL in SQL)
        cleaned_df["text_date"] = cleaned_df["text_date"].apply(
            lambda x: None if pd.isna(x) else str(x)
        )

        insert_query = """
        INSERT INTO Medical_DataWarehouse 
        (channel_name, channel_title, message, text_date, emoji_used) 
        VALUES (:channel_name, :channel_title, :message, :text_date, :emoji_used);
        """

        with engine.begin() as connection:  # ✅ Auto-commit enabled
            for _, row in cleaned_df.iterrows():
                connection.execute(
                    text(insert_query),
                    {
                        "channel_name": row["channel_name"],
                        "channel_title": row["channel_title"],
                        "message": row["message"],
                        "text_date": row["text_date"],
                        "emoji_used": row["emoji_used"],
                    },
                )

        logging.info(f"✅ {len(cleaned_df)} records inserted into PostgreSQL database.")
    except Exception as e:
        logging.error(f"❌ Error inserting data: {e}")
        raise
