from typing import Dict, Any
import requests

from sports_api.config import Config
from sports_api.endpoints.searches import Searches


class SearchService:
    """
    Service class for handling search-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def __init__(self, config: Config):
        self.config = config
        self.searches = Searches()

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

    def search_team_by_name(self, name: str) -> Dict[str, Any]:
        """
        Search for a team by name.

        :param name: Team name to search for
        :return: Search results
        """
        endpoint = self.searches.search_team_by_name(name)
        return self._make_request(endpoint)

    def search_team_by_shortcode(self, shortcode: str) -> Dict[str, Any]:
        """
        Search for a team by shortcode.

        :param shortcode: Team shortcode to search for (e.g., 'ARS' for Arsenal)
        :return: Search results
        """
        endpoint = self.searches.search_team_by_shortcode(shortcode)
        return self._make_request(endpoint)

    def search_player_by_name(self, name: str) -> Dict[str, Any]:
        """
        Search for a player by name.

        :param name: Player name to search for
        :return: Search results
        """
        endpoint = self.searches.search_player_by_name(name)
        return self._make_request(endpoint)

    def search_event_by_name(self, event_name: str) -> Dict[str, Any]:
        """
        Search for an event by name.

        :param event_name: Event name to search for
        :return: Search results
        """
        endpoint = self.searches.search_event_by_event_name(event_name)
        return self._make_request(endpoint)

    def search_event_by_file_name(self, file_name: str) -> Dict[str, Any]:
        """
        Search for an event by file name.

        :param file_name: Event file name to search for
        :return: Search results
        """
        endpoint = self.searches.search_event_by_file_name(file_name)
        return self._make_request(endpoint)

    def search_venue_by_name(self, name: str) -> Dict[str, Any]:
        """
        Search for a venue by name.

        :param name: Venue name to search for
        :return: Search results
        """
        endpoint = self.searches.search_venue_by_name(name)
        return self._make_request(endpoint)

    # Premium methods - these will only work with a premium API key
    def search_all_players_from_team(self, team: str) -> Dict[str, Any]:
        """
        Search for all players from a team. Requires premium API key.

        :param team: Team name
        :return: All players from the team
        """
        endpoint = self.searches.search_all_players_from_team(team)
        return self._make_request(endpoint)
