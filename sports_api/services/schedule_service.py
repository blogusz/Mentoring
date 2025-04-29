from typing import Dict, Any, Optional
import requests

from sports_api.config import Config
from sports_api.services.decorators import premium_required


class ScheduleService:
    """
    Service class for handling schedule-related operations.
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
    def get_last_5_events_by_team(self, team_id: int) -> Dict[str, Any]:
        """
        Get the last 5 events for a team (limited to home team for free tier).

        :param team_id: Team ID, e.g. 133602
        :return: Last 5 events
        """
        endpoint = f'eventslast.php?id={team_id}'
        return self._make_request(endpoint)

    def get_events_by_round(self, league_id: int, round_number: int, season: str) -> Dict[str, Any]:
        """
        Get events for a specific round in a league by league id/round/season.

        :param league_id: League ID, e.g. 4328
        :param round_number: Round number, e.g. 38
        :param season: Season, e.g. '2014-2015'
        :return: Events in the round

        \n Note: Special round numbers:
          - Round 125 = Quarter-Final
          - Round 150 = Semi-Final
          - Round 160 = Playoff
          - Round 170 = Playoff Semi-Final
          - Round 180 = Playoff Final
          - Round 200 = Final
          - Round 500 = Pre-Season
        """
        endpoint = f'eventsround.php?id={league_id}&r={round_number}&s={season}'
        return self._make_request(endpoint)

    def get_events_in_league_by_season(self, league_id: int, season: str) -> Dict[str, Any]:
        """
        Get all events in a league for a season (Free tier limited to 100 events).

        :param league_id: League ID, e.g. 4328
        :param season: Season, e.g. '2014-2015'
        :return: Events in the league for the season
        """
        endpoint = f'eventsseason.php?id={league_id}&s={season}'
        return self._make_request(endpoint)

    # Premium methods - these will only work with a premium API key
    @premium_required
    def get_next_5_events_by_team(self, team_id: int) -> Dict[str, Any]:
        """
        Get the next 5 events for a team.

        :param team_id: Team ID, e.g. 133602
        :return: Next 5 events
        """
        endpoint = f'eventsnext.php?id={team_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_next_25_events_by_league(self, league_id: int) -> Dict[str, Any]:
        """
        Get the next 25 events for a league.

        :param league_id: League ID, e.g. 4328
        :return: Next 25 events
        """
        endpoint = f'eventsnextleague.php?id={league_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_last_15_events_by_league(self, league_id: int) -> Dict[str, Any]:
        """
        Get the last 15 events for a league.

        :param league_id: League ID, e.g. 4328
        :return: Last 15 events
        """
        endpoint = f'eventspastleague.php?id={league_id}'
        return self._make_request(endpoint)

    @premium_required
    def get_events_on_day(self, day: str, sport: Optional[str] = None, league: Optional[str] = None) -> Dict[str, Any]:
        """
        Get events on a specific day.

        :param day: Day in YYYY-MM-DD format
        :param sport: Optional sport name, e.g. 'Soccer'
        :param league: Optional league ID or name, e.g. '4356' or 'Australian_A-League'
        :return: Events on the day

        Examples:
          \n eventsday.php?d=2014-10-10
          \n eventsday.php?d=2014-10-10&s=Soccer
          \n eventsday.php?d=2014-10-10&l=4356
          \n eventsday.php?d=2014-10-10&l=Australian_A-League
        """
        params = [f"d={day}"]
        if sport:
            params.append(f"s={sport}")
        if league:
            params.append(f"l={league}")
        endpoint = "eventsday.php?" + "&".join(params)
        return self._make_request(endpoint)

    @premium_required
    def get_tv_events_on_day(self, day: Optional[str] = None, sport: Optional[str] = None,
                             station_country: Optional[str] = None, channel: Optional[str] = None) -> Dict[str, Any]:
        """
        Get TV events on a specific day (By Sport/Date/TV Station Country).

        :param day: Optional day in YYYY-MM-DD format
        :param sport: Optional sport name
        :param station_country: Optional TV station country
        :param channel: Optional channel name
        :return: TV events on the day

        Examples:
          \n eventstv.php?d=2018-07-07
          \n eventstv.php?d=2018-07-07&s=Fighting
          \n eventstv.php?d=2019-09-28&a=United%20Kingdom&s=Cycling
          \n eventstv.php?c=Peacock_Premium
        """
        params = []
        if day:
            params.append(f"d={day}")
        if sport:
            params.append(f"s={sport}")
        if station_country:
            params.append(f"a={station_country}")
        if channel:
            params.append(f"c={channel}")
        endpoint = "eventstv.php?" + "&".join(params)
        return self._make_request(endpoint)
