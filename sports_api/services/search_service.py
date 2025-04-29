from typing import Dict, Any

from sports_api.services.base_service import BaseService
from sports_api.services.decorators import premium_required


class SearchService(BaseService):
    """
    Service class for handling search-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def search_team_by_name(self, name: str) -> Dict[str, Any]:
        """
        Search for a team by name.

        :param name: Team name to search for, e.g. 'Arsenal'
        :return: Search results
        """
        endpoint = f'searchteams.php?t={name}'
        return self._make_request(endpoint)

    def search_team_by_shortcode(self, shortcode: str) -> Dict[str, Any]:
        """
        Search for a team by shortcode.

        :param shortcode: Team shortcode to search for (e.g., 'ARS' for Arsenal)
        :return: Search results
        """
        endpoint = f'searchteams.php?t={shortcode}'
        return self._make_request(endpoint)

    def search_player_by_name(self, name: str) -> Dict[str, Any]:
        """
        Search for a player by name.

        :param name: Player name to search for (e.g. 'Danny'/'Welbeck'/'Danny_Welbeck')
        :return: Search results
        """
        endpoint = f'searchplayers.php?p={name}'
        return self._make_request(endpoint)

    def search_event_by_name(self, event_name: str) -> Dict[str, Any]:
        """
        Search for an event by name.

        :param event_name: Event name to search for (e.g. 'Arsenal_vs_Chelsea', 'Arsenal_vs_Chelsea&s=2016-2017')
        :return: Search results
        """
        endpoint = f'searchevents.php?e={event_name}'
        return self._make_request(endpoint)

    def search_event_by_file_name(self, file_name: str) -> Dict[str, Any]:
        """
        Search for an event by file name.

        :param file_name: Event file name to search for, e.g. 'English_Premier_League_2015-04-26_Arsenal_vs_Chelsea'
        :return: Search results
        """
        endpoint = f'searchfilename.php?e={file_name}'
        return self._make_request(endpoint)

    def search_venue_by_name(self, name: str) -> Dict[str, Any]:
        """
        Search for a venue by name.

        :param name: Venue name to search for, e.g. 'Wembley'
        :return: Search results
        """
        endpoint = f'searchvenues.php?t={name}'
        return self._make_request(endpoint)

    # Premium methods - these will only work with a premium API key
    @premium_required
    def search_all_players_from_team(self, team: str) -> Dict[str, Any]:
        """
        Search for all players from a team.

        :param team: Team name, e.g. 'Arsenal'
        :return: All players from the team
        """
        endpoint = f'searchplayers.php?t={team}'
        return self._make_request(endpoint)
