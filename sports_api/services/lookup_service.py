from typing import Dict, Any

from sports_api.services.base_service import BaseService
from sports_api.services.decorators import premium_required


class LookupService(BaseService):
    """
    Service class for handling lookup-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def get_player_details(self, player_id: int) -> Dict[str, Any]:
        endpoint = f'lookupplayer.php?id={player_id}'
        return self._make_request(endpoint)

    def get_venue_details(self, venue_id: int) -> Dict[str, Any]:
        endpoint = f'lookupvenue.php?id={venue_id}'
        return self._make_request(endpoint)

    def get_player_honours(self, player_id: int) -> Dict[str, Any]:
        endpoint = f'lookuphonours.php?id={player_id}'
        return self._make_request(endpoint)

    def get_player_milestones(self, player_id: int) -> Dict[str, Any]:
        endpoint = f'lookupmilestones.php?id={player_id}'
        return self._make_request(endpoint)

    def get_player_former_teams(self, player_id: int) -> Dict[str, Any]:
        endpoint = f'lookupformerteams.php?id={player_id}'
        return self._make_request(endpoint)

    def get_player_contracts(self, player_id: int) -> Dict[str, Any]:
        endpoint = f'lookupcontracts.php?id={player_id}'
        return self._make_request(endpoint)

    def get_event_player_results(self, event_id: int) -> Dict[str, Any]:
        endpoint = f'eventresults.php?id={event_id}'
        return self._make_request(endpoint)

    def get_league_table(self, league_id: int, season: str) -> Dict[str, Any]:
        endpoint = f'lookuptable.php?l={league_id}&s={season}'
        return self._make_request(endpoint)

    def get_team_equipment(self, team_id: int) -> Dict[str, Any]:
        endpoint = f'lookupequipment.php?id={team_id}'
        return self._make_request(endpoint)

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
