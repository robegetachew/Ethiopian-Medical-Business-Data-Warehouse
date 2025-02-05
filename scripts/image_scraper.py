import os
import logging
import re
from dotenv import load_dotenv
from telethon.sync import TelegramClient

# Load environment variables
load_dotenv()

# Define the project root directory (one level above `scripts/`)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure the logs directory exists at the project root
log_dir = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(log_dir, exist_ok=True)

# Configure logging to store logs outside the scripts folder
log_file = os.path.join(log_dir, "scraping.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("🚀 Telegram Image scraper started successfully.")

# Telegram API setup
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE_NUMBER")

# Ensure the image directory exists at the project root level
IMAGE_FOLDER = os.path.join(PROJECT_ROOT, "data", "images")
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Channels to scrape images from
image_channels = ["https://t.me/CheMed123", "https://t.me/lobelia4cosmetics"]

# Initialize Telegram client
client = TelegramClient("session_name", api_id, api_hash)


async def scrape_images():
    """Scrape images from Telegram channels and save them locally."""
    await client.start(phone_number)

    for channel in image_channels:
        try:
            entity = await client.get_entity(channel)
            messages = await client.get_messages(entity, limit=50)

            for msg in messages:
                if msg.photo:
                    # Sanitize channel name (remove 'https://' and replace invalid characters)
                    sanitized_channel = re.sub(r"https://t.me/|[^a-zA-Z0-9_]", "_", channel)
                    
                    # Format date to remove invalid characters
                    formatted_date = msg.date.strftime("%Y-%m-%d_%H-%M-%S")  # Converts to "YYYY-MM-DD_HH-MM-SS"
                    
                    # Define the filename with a sanitized channel name and formatted date
                    filename = os.path.join(IMAGE_FOLDER, f"{sanitized_channel}_{formatted_date}.jpg")

                    # Download and save the image
                    await client.download_media(msg.photo, filename)
                    
                    # Logging and print statement
                    logging.info(f"✅ Downloaded image from {channel} - {filename}")
                    print(f"✅ Image saved: {filename}")  # Print confirmation

        except Exception as e:
            logging.error(f"❌ Error scraping images from {channel}: {e}")
            print(f"❌ Error scraping images from {channel}: {e}")


# Run the scraper
with client:
    client.loop.run_until_complete(scrape_images())
