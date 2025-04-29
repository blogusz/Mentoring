from typing import Dict, Any
import requests

from sports_api.config import Config
from sports_api.endpoints.decorators import premium_required


class LookupService:
    """
    Service class for handling lookup-related operations.
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

    # Non-premium methods
    def get_player_details(self, player_id: int) -> Dict[str, Any]:
        """
        Get details for a player.

        :param player_id: Player ID, e.g. 34145937
        :return: Player details
        """
        endpoint = f'lookupplayer.php?id={player_id}'
        return self._make_request(endpoint)

    def get_venue_details(self, venue_id: int) -> Dict[str, Any]:
        """
        Get details for a venue.

        :param venue_id: Venue ID, e.g. 16163
        :return: Venue details
        """
        endpoint = f'lookupvenue.php?id={venue_id}'
        return self._make_request(endpoint)

    def get_player_honours(self, player_id: int) -> Dict[str, Any]:
        """
        Get honours for a player.

        :param player_id: Player ID, e.g. 34147178
        :return: Player honours
        """
        endpoint = f'lookuphonours.php?id={player_id}'
        return self._make_request(endpoint)

    def get_player_milestones(self, player_id: int) -> Dict[str, Any]:
        """
        Get milestones for a player.

        :param player_id: Player ID, e.g. 34161397
        :return: Player milestones
        """
        endpoint = f'lookupmilestones.php?id={player_id}'
        return self._make_request(endpoint)

    def get_player_former_teams(self, player_id: int) -> Dict[str, Any]:
        """
        Get former teams for a player.

        :param player_id: Player ID, e.g. 34147178
        :return: Player former teams
        """
        endpoint = f'lookupformerteams.php?id={player_id}'
        return self._make_request(endpoint)

    def get_player_contracts(self, player_id: int) -> Dict[str, Any]:
        """
        Get contracts for a player.

        :param player_id: Player ID
        :return: Player contracts
        """
        endpoint = f'lookupcontracts.php?id={player_id}'
        return self._make_request(endpoint)

    def get_event_player_results(self, event_id: int) -> Dict[str, Any]:
        """
        Get player results for an event.

        :param event_id: Event ID, e.g. 652890
        :return: Event player results
        """
        endpoint = f'eventresults.php?id={event_id}'
        return self._make_request(endpoint)

    def get_league_table(self, league_id: int, season: str) -> Dict[str, Any]:
        """
        Get the league table for a league and season.

        :param league_id: League ID, e.g. 4328
        :param season: Season, e.g. '2020-2021'
        :return: League table
        """
        endpoint = f'lookuptable.php?l={league_id}&s={season}'
        return self._make_request(endpoint)

    def get_team_equipment(self, team_id: int) -> Dict[str, Any]:
        """
        Get equipment (kits) for a team.

        :param team_id: Team ID, e.g. 133597
        :return: Team equipment
        """
        endpoint = f'lookupequipment.php?id={team_id}'
        return self._make_request(endpoint)

    # Premium methods - these will only work with a premium API key
    @premium_required
    def get_league_details(self, league_id: int) -> Dict[str, Any]:
        """
        Get details for a league.

        :param league_id: League ID, e.g. 4346
        :return: League details
        """
        endpoint = f'lookupleague.php?id={league_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_team_details(self, team_id: int) -> Dict[str, Any]:
        """
        Get details for a team.

        :param team_id: Team ID, e.g. 133604
        :return: Team details
        """
        endpoint = f'lookupteam.php?id={team_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_event_details(self, event_id: int) -> Dict[str, Any]:
        """
        Get details for an event.

        :param event_id: Event ID, e.g. 441613
        :return: Event details
        """
        endpoint = f'lookupevent.php?id={event_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_event_statistics(self, event_id: int) -> Dict[str, Any]:
        """
        Get statistics for an event.

        :param event_id: Event ID, e.g. 1032723
        :return: Event statistics
        """
        endpoint = f'lookupeventstats.php?id={event_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_event_lineup(self, event_id: int) -> Dict[str, Any]:
        """
        Get lineup for an event.

        :param event_id: Event ID, e.g. 1032723
        :return: Event lineup
        """
        endpoint = f'lookuplineup.php?id={event_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_event_timeline(self, event_id: int) -> Dict[str, Any]:
        """
        Get timeline for an event.

        :param event_id: Event ID, e.g. 1032718
        :return: Event timeline
        """
        endpoint = f'lookuptimeline.php?id={event_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_event_tv(self, event_id: int) -> Dict[str, Any]:
        """
        Get TV information for an event.

        :param event_id: Event ID, e.g. 584911
        :return: Event TV information
        """
        endpoint = f'lookuptv.php?id={event_id}'
        return self._make_request(endpoint)
