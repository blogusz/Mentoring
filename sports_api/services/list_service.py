from typing import Dict, Any, Optional

from sports_api.services.base_service import BaseService
from sports_api.services.decorators import premium_required


class ListService(BaseService):
    """
    Service class for handling list-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def get_all_leagues(self) -> Dict[str, Any]:
        return self._make_request('all_leagues.php')

    def get_all_countries(self) -> Dict[str, Any]:
        return self._make_request('all_countries.php')

    def get_all_leagues_in_country(self, country: str, sport: Optional[str] = None) -> Dict[str, Any]:
        """
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
        \n Example 1: search_all_teams.php?l=English%20Premier%20League
        \n Example 2: search_all_teams.php?s=Soccer&c=Spain
        """
        if sport and country:
            endpoint = f'search_all_teams.php?s={sport}&c={country}'
        else:
            endpoint = f'search_all_teams.php?l={league_name}'
        return self._make_request(endpoint)

    def get_all_users_loved_teams_and_players(self, username: str) -> Dict[str, Any]:
        endpoint = f'searchloves.php?u={username}'
        return self._make_request(endpoint)

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
