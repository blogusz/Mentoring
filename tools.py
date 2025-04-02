import os

from dotenv import load_dotenv


def load_config():
    load_dotenv()
    api_key = os.getenv('API_KEY') or 3
    base_url = f'https://www.thesportsdb.com/api/v1/json'
    return api_key, base_url
