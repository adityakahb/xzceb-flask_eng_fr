"""
    Translator which connects with IBM Watson and returns translated text for English and French
"""
import os
from xml.etree.ElementTree import VERSION
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Function to translate english text to french text

    Parameters:
        english_text (str): Text in english language

    Returns:
        str: Translated text in French or error
    """
    try:
        french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    except:
        return 'Could not process English Text'


def french_to_english(french_text):
    """
    Function to translate french text to english text

    Parameters:
        french_text (str): Text in french language

    Returns:
        str: Translated text in English or error
    """
    try:
        english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    except:
        return 'Could not process French Text'
