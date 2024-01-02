from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Keys
scrape_API_KEY = os.getenv("SCRAPE_API_KEY")

# Telegram API details
telegram_api_key = os.getenv("TELEGRAM_API_KEY")
telegram_user_name = 'chuck_norris_2396_bot'

# Azure Translator API details
subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY")
endpoint = os.getenv("AZURE_ENDPOINT")
region = os.getenv("AZURE_REGION")

# Nums
SET_REQUEST = 1
JOKE_NUM = 2
UNDEFINED_MSG = 3

# User Messages
SET_LANG_MSG = "You have to set language first!"
DONT_UNDERSTAND_MSG = "I dont understand...."
CHOOSE_LANG_MSG = "Hey! please choose a language"

