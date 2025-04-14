class Config:
    def __init__(self, api_key=None, base_url=None):
        if not (api_key and base_url):
            self._load_config()
        else:
            self.api_key = api_key
            self.base_url = base_url

        print(f'Created Config instance with fields:\n - api_key = ######\n - base_url = {self.base_url}')

    @staticmethod
    def _load_config_from_dotenv_file():
        from dotenv import load_dotenv
        import os

        load_dotenv()

        return os.getenv('API_KEY') or 3, os.getenv('BASE_URL')

    def _load_config(self):
        self.api_key, self.base_url = self._load_config_from_dotenv_file()

    def get_credentials(self):
        return self.api_key, self.base_url
