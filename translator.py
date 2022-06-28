#!/usr/bin/python3
import requests

# Change the languages here, must use the ISO Standard Names
source_language = 'en'
language_to_translate = 'de'

# Function to translate the text
def translate(text):
    text_to_translate = text
    languages_pair = source_language + '|' + language_to_translate
    req_params = {'q': text_to_translate, 'langpair': languages_pair}
    api_url = 'https://api.mymemory.translated.net/get'
    req = requests.get(api_url, params= req_params)
    req_dict = req.json()
    res_data = req_dict['responseData']
    translated_text = res_data['translatedText']
    print(translated_text)

if (__name__ == "__main__"):
    text = input()
    translate(text)