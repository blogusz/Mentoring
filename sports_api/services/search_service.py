from typing import Dict, Any

from sports_api.services.base_service import BaseService
from sports_api.services.decorators import premium_required


class SearchService(BaseService):
    """
    Service class for handling search-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def search_team_by_name(self, name: str) -> Dict[str, Any]:
        endpoint = f'searchteams.php?t={name}'
        return self._make_request(endpoint)

    def search_team_by_shortcode(self, shortcode: str) -> Dict[str, Any]:
        endpoint = f'searchteams.php?t={shortcode}'
        return self._make_request(endpoint)

    def search_player_by_name(self, name: str) -> Dict[str, Any]:
        endpoint = f'searchplayers.php?p={name}'
        return self._make_request(endpoint)

    def search_event_by_name(self, event_name: str) -> Dict[str, Any]:
        endpoint = f'searchevents.php?e={event_name}'
        return self._make_request(endpoint)

    def search_event_by_file_name(self, file_name: str) -> Dict[str, Any]:
        endpoint = f'searchfilename.php?e={file_name}'
        return self._make_request(endpoint)

    def search_venue_by_name(self, name: str) -> Dict[str, Any]:
        endpoint = f'searchvenues.php?t={name}'
        return self._make_request(endpoint)

    @premium_required
    def search_all_players_from_team(self, team: str) -> Dict[str, Any]:
        """
        Search for all players from a team.

        :param team: Team name, e.g. 'Arsenal'
        :return: All players from the team
        """
        endpoint = f'searchplayers.php?t={team}'
        return self._make_request(endpoint)
