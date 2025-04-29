from typing import Dict, Any
import requests

from sports_api.config import Config


class BaseService:
    """
    Base service class that provides common functionality for all service classes.
    All service classes should inherit from this class.
    """
    
    def __init__(self, config: Config):
        """
        Initialize the base service.
        
        :param config: Config object with API credentials
        """
        self.config = config
    
    def _make_request(self, endpoint: str) -> Dict[str, Any]:
        """
        Make a request to the API.
        
        :param endpoint: API endpoint to call
        :return: JSON response as a dictionary
        """
        api_key, base_url = self.config.get_credentials()
        url = f'{base_url}/{api_key}/{endpoint}'
        
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
