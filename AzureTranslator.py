import requests
import uuid
UNDEFINED_LANG_ERROR = "Can't find the language you requested. Please try again"


class AzureTranslator:
    def __init__(self, endpoint, subscription_key, region):
        self.endpoint = endpoint
        self.subscription_key = subscription_key
        self.region = region
        self.lang_dic = self.get_language_mapping()

    def get_language_mapping(self):
        # Endpoint for language list API
        language_api_endpoint = f"{self.endpoint}/languages?api-version=3.0"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
        }
        # Make a GET request to the language list API
        response = requests.get(language_api_endpoint, headers=headers)
        languages = response.json()['translation']
        language_mapping = {languages[lang]['name'].lower(): lang.lower() for lang in languages}
        return language_mapping

    def translate_text(self, text, to_language):
        try:
            lang_code = self.lang_dic[to_language.lower()]
        except KeyError as e:
            return UNDEFINED_LANG_ERROR

        translation_url = f"{self.endpoint}/translate?api-version=3.0&to={lang_code}"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Ocp-Apim-Subscription-Region': self.region,
            'Content-Type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        body = [{'text': text}]
        response = requests.post(translation_url, headers=headers, json=body)

        translated_text = response.json()[0]['translations'][0]['text']
        return translated_text
