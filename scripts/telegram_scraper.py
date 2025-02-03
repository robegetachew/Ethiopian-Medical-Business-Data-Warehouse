import os
import logging
import pandas as pd
from dotenv import load_dotenv
from telethon.sync import TelegramClient

# Load environment variables
load_dotenv()

# Define the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure the logs directory exists at the project root
log_dir = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
log_file = os.path.join(log_dir, "scraping.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("🚀 Telegram message scraper started successfully.")

# Load Telegram API credentials
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE_NUMBER")

# Define the directory to store scraped text data
TEXT_DATA_DIR = os.path.join(PROJECT_ROOT, "data", "messages")
os.makedirs(TEXT_DATA_DIR, exist_ok=True)

# Define the file path for saving messages
text_data_path = os.path.join(TEXT_DATA_DIR, "scraped_messages.csv")

# Ensure the CSV file exists with proper headers
if not os.path.exists(text_data_path):
    pd.DataFrame(columns=["channel", "date", "text"]).to_csv(text_data_path, index=False)

print(f"📂 Data will be saved at: {text_data_path}")

# List of Telegram channels to scrape
channels = [
    "https://t.me/DoctorsET",
    "https://t.me/CheMed123",
    "https://t.me/lobelia4cosmetics",
    "https://t.me/yetenaweg",
    "https://t.me/EAHCI",
]

# Initialize Telegram client
client = TelegramClient("session_name", api_id, api_hash)


async def scrape_messages():
    """Scrape messages from Telegram channels and save them to a CSV file."""
    await client.start(phone_number)

    all_messages = []  # Store scraped messages

    for channel in channels:
        try:
            entity = await client.get_entity(channel)  # Get channel entity
            messages = await client.get_messages(entity, limit=100)  # Fetch latest 100 messages

            for msg in messages:
                all_messages.append(
                    {
                        "channel": channel,
                        "date": msg.date.strftime("%Y-%m-%d %H:%M:%S"),
                        "text": msg.text if msg.text else "[No Text]",
                    }
                )

            logging.info(f"✅ Scraped {len(messages)} messages from {channel}")
            print(f"✅ Scraped {len(messages)} messages from {channel}")

        except Exception as e:
            logging.error(f"❌ Error scraping {channel}: {e}")
            print(f"❌ Error scraping {channel}: {e}")

    # Convert scraped messages into a DataFrame and save to CSV
    df = pd.DataFrame(all_messages)
    if not df.empty:
        df.to_csv(text_data_path, mode="a", header=False, index=False)
        logging.info("📌 Messages saved successfully!")
        print("📌 Messages saved successfully!")

# Run the scraper
with client:
    client.loop.run_until_complete(scrape_messages())
