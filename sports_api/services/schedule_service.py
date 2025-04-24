from typing import Dict, Any, Optional
import requests

from sports_api.config import Config
from sports_api.endpoints.schedules import Schedules


class ScheduleService:
    """
    Service class for handling schedule-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def __init__(self, config: Config):
        self.config = config
        self.schedules = Schedules()

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
    def get_last_5_events_by_team(self, team_id: int) -> Dict[str, Any]:
        """
        Get the last 5 events for a team.

        :param team_id: Team ID
        :return: Last 5 events
        """
        endpoint = self.schedules.events_last_5_by_team_id(team_id)
        return self._make_request(endpoint)

    def get_events_by_round(self, league_id: int, round_number: int, season: str) -> Dict[str, Any]:
        """
        Get events for a specific round in a league.

        :param league_id: League ID
        :param round_number: Round number
        :param season: Season
        :return: Events in the round
        """
        endpoint = self.schedules.events_by_round(league_id, round_number, season)
        return self._make_request(endpoint)

    def get_events_in_league_by_season(self, league_id: int, season: str) -> Dict[str, Any]:
        """
        Get all events in a league for a season.

        :param league_id: League ID
        :param season: Season
        :return: Events in the league for the season
        """
        endpoint = self.schedules.events_in_league_by_season(league_id, season)
        return self._make_request(endpoint)

    # Premium methods - these will only work with a premium API key
    def get_next_5_events_by_team(self, team_id: int) -> Dict[str, Any]:
        """
        Get the next 5 events for a team. Requires premium API key.

        :param team_id: Team ID
        :return: Next 5 events
        """
        endpoint = self.schedules.events_next_5_by_team_id(team_id)
        return self._make_request(endpoint)

    def get_next_25_events_by_league(self, league_id: int) -> Dict[str, Any]:
        """
        Get the next 25 events for a league. Requires premium API key.

        :param league_id: League ID
        :return: Next 25 events
        """
        endpoint = self.schedules.events_next_25_by_league_id(league_id)
        return self._make_request(endpoint)

    def get_last_15_events_by_league(self, league_id: int) -> Dict[str, Any]:
        """
        Get the last 15 events for a league. Requires premium API key.

        :param league_id: League ID
        :return: Last 15 events
        """
        endpoint = self.schedules.events_last_15_by_league_id(league_id)
        return self._make_request(endpoint)

    def get_events_on_day(self, day: str, sport: Optional[str] = None, league: Optional[str] = None) -> Dict[str, Any]:
        """
        Get events on a specific day. Requires premium API key.

        :param day: Day in YYYY-MM-DD format
        :param sport: Optional sport name
        :param league: Optional league ID or name
        :return: Events on the day
        """
        endpoint = self.schedules.events_on_day(day, sport, league)
        return self._make_request(endpoint)

    def get_tv_events_on_day(self, day: Optional[str] = None, sport: Optional[str] = None,
                             station_country: Optional[str] = None, channel: Optional[str] = None) -> Dict[str, Any]:
        """
        Get TV events on a specific day. Requires premium API key.

        :param day: Optional day in YYYY-MM-DD format
        :param sport: Optional sport name
        :param station_country: Optional TV station country
        :param channel: Optional channel name
        :return: TV events on the day
        """
        endpoint = self.schedules.tv_events_on_day(day, sport, station_country, channel)
        return self._make_request(endpoint)
