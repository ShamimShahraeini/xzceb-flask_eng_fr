import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = 'LoEvljIma5xFK405J-FFVlxIsFNiqbMETjSl8bdLLcyh'
URL = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/9057d64a-3e76-4e18-83e8-78b6ae4bd172'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)


def english_to_french(english_text):
    translation_response = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    )
    translation = translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation_response = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    )
    translation = translation_response.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
