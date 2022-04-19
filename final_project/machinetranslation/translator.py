import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='0.1',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')


def french_to_english(frenchtext):
    """
    Translate French to English
    """
    englishtext = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()
    return englishtext.get('translations')[0].get('translations')



def english_to_french(englishtext):
    """
    Translate English to French
    """
    frenchtext = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()
    return frenchtext.get('translations')[0].get('translations')


