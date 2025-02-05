# Ethiopian-Medical-Business-Data-Warehouse

A comprehensive data warehouse project for scraping, cleaning, and analyzing Ethiopian medical business data from Telegram channels. This project includes data collection pipelines, data transformation using DBT, object detection with YOLO, and a FastAPI interface for data access.


# **Task 1: Data Scraping and Collection Pipeline**

### **Overview**
This project aims to develop a data scraping and collection pipeline to extract relevant data from public Telegram channels related to Ethiopian medical businesses. The project will utilize the Telegram API and custom scripts for data extraction, focusing on both textual data and images for object detection.

### **Channels to Scrape**
The following Telegram channels will be targeted for data scraping:

- [Doctors Ethiopia](https://t.me/DoctorsET)
- [Chemed Telegram Channel](https://t.me/Chemed)
- [Lobelia Pharmacy and Cosmetics](https://t.me/lobelia4cosmetics)
- [Yetenaweg](https://t.me/yetenaweg)
- [Ethio-American Medical Trainings](https://t.me/EAHCI)

### Objectives
1. **Text Data Extraction**: Scrape and collect textual data from the specified Telegram channels.
2. **Image Collection**: Gather images from the targeted channels for future object detection tasks.

## **Completed Tasks**

### 1. **Telegram Data Scraping**
- Use the `telethon` library in Python to interact with the Telegram API.
- Develop scripts to extract data from the specified channels.
- Alternatively, export content using the Telegram application if necessary.

### 2. **Image and Data Collection**
- Focus on collecting images specifically from:
  - Chemed Telegram Channel
  - Lobelia Pharmacy and Cosmetics
- Ensure that the images collected are suitable for object detection tasks.

### 3. **Storing Raw Data**
- **Initial Storage**: Store the scraped data in a temporary location such as a local database or flat files for further processing.

### 4. **Monitoring and Logging**
- Implement logging to monitor the scraping process:
  - Track progress
  - Capture errors
  - Log important events during the scraping operation


## **Conclusion**
Upon completion of this task, the pipeline will effectively scrape and collect data from the specified Telegram channels, providing valuable insights into Ethiopian medical businesses. The collected data will be stored for further analysis and potential machine learning applications.


# Project Structure

```
+---.github
| └── workflows
| └── blank.yml
+---.vscode
| └── settings.json
+---api
| ├── init.py
+---Medical_Business_Data_Warehouse
| | ├── analyses
| | ├── dbt_packages
| | ├── logs
| | | ├── dbt.log
| | ├── macros
| | ├── models
| | | ├── example
| | | | ├── aggregate_messages_by_channel.sql
| | | | ├── calculate_message_length.sql
| | | | ├── convert_text_date_to_message_date.sql
| | | | ├── filter_messages_with_emojis.sql
| | | | ├── raw_messages.sql
| | | | ├── schema.yml
| | | | ├── select_cleaned_data.sql
| | | | ├── transformed_messages.sql
| | ├── seeds
| | ├── snapshots
| | ├── target
| | ├── tests
| └── .gitignore
| └── dbt_project.yml
| └── README.md
+---notebooks
| ├── init.ipynb
| ├── data_cleaning.ipynb
| └── README.md
| └── telegram_message_scrapper.ipynb
+---scripts
| ├── init.py
| └── README.md
| ├── data_cleaning.py
| ├── database_setup.py
| ├── image_scraper.py
| ├── telegram_scraper.py
+---src
| └── README.md
| └── init.py
+---tests
| └── init.py
| ├── README.md
| └── test_scraper.py
| ├── .gitignore
| ├── LICENSE
| ├── README.md
| └── requirements.txt
```