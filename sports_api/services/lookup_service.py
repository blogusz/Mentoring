from typing import Dict, Any
import requests

from sports_api.config import Config
from sports_api.endpoints.lookups import Lookups


class LookupService:
    """
    Service class for handling lookup-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def __init__(self, config: Config):
        self.config = config
        self.lookups = Lookups()

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

    # Non-premium methods
    def get_player_details(self, player_id: int) -> Dict[str, Any]:
        """
        Get details for a player.

        :param player_id: Player ID
        :return: Player details
        """
        endpoint = self.lookups.lookup_player_details_by_id(player_id)
        return self._make_request(endpoint)

    def get_venue_details(self, venue_id: int) -> Dict[str, Any]:
        """
        Get details for a venue.

        :param venue_id: Venue ID
        :return: Venue details
        """
        endpoint = self.lookups.lookup_venue_details_by_id(venue_id)
        return self._make_request(endpoint)

    def get_player_honours(self, player_id: int) -> Dict[str, Any]:
        """
        Get honours for a player.

        :param player_id: Player ID
        :return: Player honours
        """
        endpoint = self.lookups.lookup_player_honours_by_id(player_id)
        return self._make_request(endpoint)

    def get_player_milestones(self, player_id: int) -> Dict[str, Any]:
        """
        Get milestones for a player.

        :param player_id: Player ID
        :return: Player milestones
        """
        endpoint = self.lookups.lookup_player_milestones_by_id(player_id)
        return self._make_request(endpoint)

    def get_player_former_teams(self, player_id: int) -> Dict[str, Any]:
        """
        Get former teams for a player.

        :param player_id: Player ID
        :return: Player former teams
        """
        endpoint = self.lookups.lookup_player_former_teams_by_id(player_id)
        return self._make_request(endpoint)

    def get_player_contracts(self, player_id: int) -> Dict[str, Any]:
        """
        Get contracts for a player.

        :param player_id: Player ID
        :return: Player contracts
        """
        endpoint = self.lookups.lookup_player_contracts_by_id(player_id)
        return self._make_request(endpoint)

    def get_event_player_results(self, event_id: int) -> Dict[str, Any]:
        """
        Get player results for an event.

        :param event_id: Event ID
        :return: Event player results
        """
        endpoint = self.lookups.lookup_event_player_results_by_event_id(event_id)
        return self._make_request(endpoint)

    def get_league_table(self, league_id: int, season: str) -> Dict[str, Any]:
        """
        Get the league table for a league and season.

        :param league_id: League ID
        :param season: Season
        :return: League table
        """
        endpoint = self.lookups.lookup_table_by_league_and_season(league_id, season)
        return self._make_request(endpoint)

    def get_team_equipment(self, team_id: int) -> Dict[str, Any]:
        """
        Get equipment (kits) for a team.

        :param team_id: Team ID
        :return: Team equipment
        """
        endpoint = self.lookups.lookup_equipment_by_team_id(team_id)
        return self._make_request(endpoint)

    # Premium methods - these will only work with a premium API key
    def get_league_details(self, league_id: int) -> Dict[str, Any]:
        """
        Get details for a league. Requires premium API key.

        :param league_id: League ID
        :return: League details
        """
        endpoint = self.lookups.lookup_league_details_by_id(league_id)
        return self._make_request(endpoint)

    def get_team_details(self, team_id: int) -> Dict[str, Any]:
        """
        Get details for a team. Requires premium API key.

        :param team_id: Team ID
        :return: Team details
        """
        endpoint = self.lookups.lookup_team_details_by_id(team_id)
        return self._make_request(endpoint)

    def get_event_details(self, event_id: int) -> Dict[str, Any]:
        """
        Get details for an event. Requires premium API key.

        :param event_id: Event ID
        :return: Event details
        """
        endpoint = self.lookups.lookup_event_details_by_id(event_id)
        return self._make_request(endpoint)

    def get_event_statistics(self, event_id: int) -> Dict[str, Any]:
        """
        Get statistics for an event. Requires premium API key.

        :param event_id: Event ID
        :return: Event statistics
        """
        endpoint = self.lookups.lookup_event_statistics_by_id(event_id)
        return self._make_request(endpoint)

    def get_event_lineup(self, event_id: int) -> Dict[str, Any]:
        """
        Get lineup for an event. Requires premium API key.

        :param event_id: Event ID
        :return: Event lineup
        """
        endpoint = self.lookups.lookup_event_lineup_by_id(event_id)
        return self._make_request(endpoint)

    def get_event_timeline(self, event_id: int) -> Dict[str, Any]:
        """
        Get timeline for an event. Requires premium API key.

        :param event_id: Event ID
        :return: Event timeline
        """
        endpoint = self.lookups.lookup_event_timeline_by_id(event_id)
        return self._make_request(endpoint)

    def get_event_tv(self, event_id: int) -> Dict[str, Any]:
        """
        Get TV information for an event. Requires premium API key.

        :param event_id: Event ID
        :return: Event TV information
        """
        endpoint = self.lookups.lookup_event_tv_by_id(event_id)
        return self._make_request(endpoint)
