import boto3

client = boto3.client('ssm', region_name='eu-north-1')
response = client.get_parameters(
    Names=[
        'SCRAPE_API_KEY',
        'TELEGRAM_API_KEY',
        'AZURE_SUBSCRIPTION_KEY',
        'AZURE_ENDPOINT',
        'AZURE_REGION'
    ]
)

# valdiate response has data
parameter_dict = {param['Name']: param['Value'] for param in response['Parameters']}

# Keys
scrape_API_KEY = parameter_dict.get("SCRAPE_API_KEY", None)
# Telegram API details
telegram_user_name = 'chuck_norris_2396_bot'
telegram_api_key = parameter_dict.get("TELEGRAM_API_KEY", None)
# Azure Translator API details
subscription_key = parameter_dict.get("AZURE_SUBSCRIPTION_KEY", None)
endpoint = parameter_dict.get("AZURE_ENDPOINT", None)
region = parameter_dict.get("AZURE_REGION", None)

# Nums
SET_REQUEST = 1
JOKE_NUM = 2
UNDEFINED_MSG = 3
MIN_JOKE_NUM = 1
MAX_JOKE_NUM = 101

# User Messages
SET_LANG_MSG = "You have to set language first!"
DONT_UNDERSTAND_MSG = "I dont understand...."
CHOOSE_LANG_MSG = "Hey! please choose a language"
