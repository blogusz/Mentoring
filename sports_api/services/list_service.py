from typing import Dict, Any, Optional
import requests

from sports_api.config import Config
from sports_api.services.decorators import premium_required


class ListService:
    """
    Service class for handling list-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def __init__(self, config: Config):
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

    def get_all_leagues(self) -> Dict[str, Any]:
        """
        List all leagues (limited 50 on free tier).

        :return: List of leagues
        """
        return self._make_request('all_leagues.php')

    def get_all_countries(self) -> Dict[str, Any]:
        """
        Get a list of all countries.

        :return: List of countries
        """
        return self._make_request('all_countries.php')

    def get_all_leagues_in_country(self, country: str, sport: Optional[str] = None) -> Dict[str, Any]:
        """
        Get a list of all leagues in a country (limited 50 on free tier).

        :param country: Country name, e.g. 'England'
        :param sport: Optional sport name to filter by, e.g 'Soccer'
        :return: List of leagues in the country

        \n Example 1: search_all_leagues.php?c=England
        \n Example 2: search_all_leagues.php?c=England&s=Soccer
        """
        if sport:
            endpoint = f'search_all_leagues.php?c={country}&s={sport}'
        else:
            endpoint = f'search_all_leagues.php?c={country}'
        return self._make_request(endpoint)

    def get_all_seasons_in_league(self, league_id: int, poster: Optional[int] = None, badge: Optional[int] = None) -> \
            Dict[str, Any]:
        """
        Get a list of all seasons in a league (or show posters and badges from seasons).

        :param league_id: League ID, e.g. '4328'
        :param poster: Optional poster ID, e.g. '1'
        :param badge: Optional badge ID, e.g. '1'
        :return: List of seasons in the league

        \n Example: search_all_leagues.php?c=England&s=Soccer
        """
        if poster:
            endpoint = f'search_all_seasons.php?id={league_id}&poster={poster}'
        elif badge:
            endpoint = f'search_all_seasons.php?id={league_id}&badge={badge}'
        else:
            endpoint = f'search_all_seasons.php?id={league_id}'
        return self._make_request(endpoint)

    def get_all_teams_in_league(self, league_name: str, sport: Optional[str] = None, country: Optional[str] = None) -> \
            Dict[str, Any]:
        """
        Get a list of all teams in a league.

        :param league_name: League name
        :param sport: Optional sport name, e.g 'Soccer'
        :param country: Optional country name, e.g. 'Spain'
        :return: List of teams in the league

        \n Example 1: search_all_teams.php?l=English%20Premier%20League
        \n Example 2: search_all_teams.php?s=Soccer&c=Spain
        """
        if sport and country:
            endpoint = f'search_all_teams.php?s={sport}&c={country}'
        else:
            endpoint = f'search_all_teams.php?l={league_name}'
        return self._make_request(endpoint)

    def get_all_users_loved_teams_and_players(self, username: str) -> Dict[str, Any]:
        """
        Get a list of all users loved teams and players.

        :param username: Username
        :return: List of loved teams and players
        """
        endpoint = f'searchloves.php?u={username}'
        return self._make_request(endpoint)

    # Premium methods - these will only work with a premium API key
    @premium_required
    def get_all_sports(self) -> Dict[str, Any]:
        """
        Get a list of all sports.

        :return: List of sports
        """
        return self._make_request('all_sports.php')

    @premium_required
    def get_all_teams_details_in_league(self, league_id: int) -> Dict[str, Any]:
        """
        Get details for all teams in a league.

        :param league_id: League ID, e.g. 4328
        :return: Details for all teams in the league
        """
        endpoint = f'lookup_all_teams.php?id={league_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_all_players_in_team(self, team_id: int) -> Dict[str, Any]:
        """
        Get all players in a team.

        :param team_id: Team ID, e.g. 133604
        :return: All players in the team
        """
        endpoint = f'lookup_all_players.php?id={team_id}'
        return self._make_request(endpoint)
