from typing import Dict, Any, Optional
import requests

from sports_api.config import Config
from sports_api.endpoints.lists import Lists


class ListService:
    """
    Service class for handling list-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def __init__(self, config: Config):
        self.config = config
        self.lists = Lists()

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

    def get_all_leagues(self) -> Dict[str, Any]:
        """
        Get a list of all leagues.

        :return: List of leagues
        """
        endpoint = self.lists.list_all_leagues()
        return self._make_request(endpoint)

    def get_all_countries(self) -> Dict[str, Any]:
        """
        Get a list of all countries.

        :return: List of countries
        """
        endpoint = self.lists.list_all_countries()
        return self._make_request(endpoint)

    def get_all_leagues_in_country(self, country: str, sport: Optional[str] = None) -> Dict[str, Any]:
        """
        Get a list of all leagues in a country.

        :param country: Country name
        :param sport: Optional sport name to filter by
        :return: List of leagues in the country
        """
        endpoint = self.lists.list_all_leagues_in_country(country, sport)
        return self._make_request(endpoint)

    def get_all_seasons_in_league(self, league_id: int, poster: Optional[int] = None, badge: Optional[int] = None) -> \
    Dict[str, Any]:
        """
        Get a list of all seasons in a league.

        :param league_id: League ID
        :param poster: Optional poster ID
        :param badge: Optional badge ID
        :return: List of seasons in the league
        """
        endpoint = self.lists.list_all_seasons_in_league(league_id, poster, badge)
        return self._make_request(endpoint)

    def get_all_teams_in_league(self, league_name: str, sport: Optional[str] = None, country: Optional[str] = None) -> \
    Dict[str, Any]:
        """
        Get a list of all teams in a league.

        :param league_name: League name
        :param sport: Optional sport name
        :param country: Optional country name
        :return: List of teams in the league
        """
        endpoint = self.lists.list_all_teams_in_league(league_name, sport, country)
        return self._make_request(endpoint)

    def get_all_users_loved_teams_and_players(self, username: str) -> Dict[str, Any]:
        """
        Get a list of all users loved teams and players.

        :param username: Username
        :return: List of loved teams and players
        """
        endpoint = self.lists.list_all_users_loved_teams_and_players(username)
        return self._make_request(endpoint)

    # Premium methods - these will only work with a premium API key
    def get_all_sports(self) -> Dict[str, Any]:
        """
        Get a list of all sports. Requires premium API key.

        :return: List of sports
        """
        endpoint = self.lists.list_all_sports()
        return self._make_request(endpoint)

    def get_all_teams_details_in_league(self, league_id: int) -> Dict[str, Any]:
        """
        Get details for all teams in a league. Requires premium API key.

        :param league_id: League ID
        :return: Details for all teams in the league
        """
        endpoint = self.lists.list_all_teams_details_in_league_by_league_id(league_id)
        return self._make_request(endpoint)

    def get_all_players_in_team(self, team_id: int) -> Dict[str, Any]:
        """
        Get all players in a team. Requires premium API key.

        :param team_id: Team ID
        :return: All players in the team
        """
        endpoint = self.lists.list_all_players_in_team_by_team_id(team_id)
        return self._make_request(endpoint)
