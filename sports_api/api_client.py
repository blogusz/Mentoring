from typing import Any, Optional, Dict

from sports_api.services.list_service import ListService
from sports_api.services.lookup_service import LookupService
from sports_api.services.rounds_service import RoundsService
from sports_api.services.schedule_service import ScheduleService
from sports_api.services.search_service import SearchService
from sports_api.config import Config


class ApiClient:
    """
    Main client for interacting with the API.
    This is the only class that users should interact with directly.
    """

    def __init__(self, config: Optional[Config] = None, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the API client.

        :param config: Optional Config object. If not provided, one will be created using api_key and base_url.
        :param api_key: Optional API key. Used only if config is not provided.
        :param base_url: Optional base URL. Used only if config is not provided.
        """
        if config:
            self.config = config
        else:
            self.config = Config(api_key, base_url)

        # Initialize services
        self._rounds_service = RoundsService(self.config)
        self._search_service = SearchService(self.config)
        self._list_service = ListService(self.config)
        self._lookup_service = LookupService(self.config)
        self._schedule_service = ScheduleService(self.config)

    def get_all_rounds(self, league_id: int, season: str, start_round: int, end_round: int,
                       output_path: str = None, output_file: str = None, save_data: bool = False) -> \
            list[Any]:
        """
        Retrieve data for consecutive rounds for the specified season and league.

        :param league_id: League ID (e.g. 4335 for Spanish La Liga)
        :param season: Season (e.g. '2024-2025')
        :param start_round: Number of the first round to retrieve
        :param end_round: Number of the last round to retrieve (inclusive)
        :param output_path: Optional override for output path from config
        :param output_file: Optional override for output filename from config
        :param save_data: Whether the data is to be saved to disk
        :return: List of round data
        """
        return self._rounds_service.get_all_rounds(
            league_id=league_id,
            season=season,
            start_round=start_round,
            end_round=end_round,
            output_path=output_path,
            output_file=output_file,
            save_data=save_data
        )

    # Search methods
    def search_team(self, name: str) -> Dict[str, Any]:
        """
        Search for a team by name.

        :param name: Team name to search for, e.g. 'Arsenal'
        :return: Search results
        """
        return self._search_service.search_team_by_name(name)

    def search_player(self, name: str) -> Dict[str, Any]:
        """
        Search for a player by name.

        :param name: Player name to search for (e.g. 'Danny'/'Welbeck'/'Danny_Welbeck')
        :return: Search results
        """
        return self._search_service.search_player_by_name(name)

    def search_event(self, event_name: str) -> Dict[str, Any]:
        """
        Search for an event by name.

        :param event_name: Event name to search for (e.g. 'Arsenal_vs_Chelsea', 'Arsenal_vs_Chelsea&s=2016-2017')
        :return: Search results
        """
        return self._search_service.search_event_by_name(event_name)

    # List methods
    def get_all_leagues(self) -> Dict[str, Any]:
        """
        Get a list of all leagues (limited to 50 on free tier).

        :return: List of leagues
        """
        return self._list_service.get_all_leagues()

    def get_all_countries(self) -> Dict[str, Any]:
        """
        Get a list of all countries.

        :return: List of countries
        """
        return self._list_service.get_all_countries()

    def get_leagues_in_country(self, country: str, sport: Optional[str] = None) -> Dict[str, Any]:
        """
        Get a list of all leagues in a country (limited to 50 on free tier).

        :param country: Country name, e.g. 'England'
        :param sport: Optional sport name to filter by, e.g 'Soccer'
        :return: List of leagues in the country
        """
        return self._list_service.get_all_leagues_in_country(country, sport)

    def get_teams_in_league(self, league_name: str, sport: Optional[str] = None, country: Optional[str] = None) -> Dict[
        str, Any]:
        """
        Get a list of all teams in a league.

        :param league_name: League name
        :param sport: Optional sport name, e.g 'Soccer'
        :param country: Optional country name, e.g. 'Spain'
        :return: List of teams in the league
        """
        return self._list_service.get_all_teams_in_league(league_name, sport, country)

    def get_seasons_in_league(self, league_id: int, poster: Optional[int] = None, badge: Optional[int] = None) -> Dict[
        str, Any]:
        """
        Get a list of all seasons in a league (or show posters and badges from seasons)..

        :param league_id: League ID, e.g. '4328'
        :param poster: Optional poster ID, e.g. '1'
        :param badge: Optional badge ID, e.g. '1'
        :return: List of seasons in the league
        """
        return self._list_service.get_all_seasons_in_league(league_id, poster, badge)

    def get_users_loved_teams_and_players(self, username: str) -> Dict[str, Any]:
        """
        Get a list of all users loved teams and players.

        :param username: Username
        :return: List of loved teams and players
        """
        return self._list_service.get_all_users_loved_teams_and_players(username)

    # Search methods - additional methods
    def search_team_by_shortcode(self, shortcode: str) -> Dict[str, Any]:
        """
        Search for a team by shortcode.

        :param shortcode: Team shortcode to search for (e.g., 'ARS' for Arsenal)
        :return: Search results
        """
        return self._search_service.search_team_by_shortcode(shortcode)

    def search_event_by_file_name(self, file_name: str) -> Dict[str, Any]:
        """
        Search for an event by file name.

        :param file_name: Event file name to search for, e.g. 'English_Premier_League_2015-04-26_Arsenal_vs_Chelsea'
        :return: Search results
        """
        return self._search_service.search_event_by_file_name(file_name)

    def search_venue(self, name: str) -> Dict[str, Any]:
        """
        Search for a venue by name.

        :param name: Venue name to search for, e.g. 'Wembley'
        :return: Search results
        """
        return self._search_service.search_venue_by_name(name)

    # Lookup methods
    def get_player_details(self, player_id: int) -> Dict[str, Any]:
        """
        Get details for a player.

        :param player_id: Player ID, e.g. 34145937
        :return: Player details
        """
        return self._lookup_service.get_player_details(player_id)

    def get_venue_details(self, venue_id: int) -> Dict[str, Any]:
        """
        Get details for a venue.

        :param venue_id: Venue ID, e.g. 16163
        :return: Venue details
        """
        return self._lookup_service.get_venue_details(venue_id)

    def get_player_honours(self, player_id: int) -> Dict[str, Any]:
        """
        Get honours for a player.

        :param player_id: Player ID, e.g. 34147178
        :return: Player honours
        """
        return self._lookup_service.get_player_honours(player_id)

    def get_player_milestones(self, player_id: int) -> Dict[str, Any]:
        """
        Get milestones for a player.

        :param player_id: Player ID, e.g. 34161397
        :return: Player milestones
        """
        return self._lookup_service.get_player_milestones(player_id)

    def get_player_former_teams(self, player_id: int) -> Dict[str, Any]:
        """
        Get former teams for a player.

        :param player_id: Player ID, e.g. 34147178
        :return: Player former teams
        """
        return self._lookup_service.get_player_former_teams(player_id)

    def get_player_contracts(self, player_id: int) -> Dict[str, Any]:
        """
        Get contracts for a player.

        :param player_id: Player ID
        :return: Player contracts
        """
        return self._lookup_service.get_player_contracts(player_id)

    def get_event_player_results(self, event_id: int) -> Dict[str, Any]:
        """
        Get player results for an event.

        :param event_id: Event ID, e.g. 652890
        :return: Event player results
        """
        return self._lookup_service.get_event_player_results(event_id)

    def get_league_table(self, league_id: int, season: str) -> Dict[str, Any]:
        """
        Get the league table for a league and season.

        :param league_id: League ID, e.g. 4328
        :param season: Season, e.g. '2020-2021'
        :return: League table
        """
        return self._lookup_service.get_league_table(league_id, season)

    def get_team_equipment(self, team_id: int) -> Dict[str, Any]:
        """
        Get equipment (kits) for a team.

        :param team_id: Team ID, e.g. 133597
        :return: Team equipment
        """
        return self._lookup_service.get_team_equipment(team_id)

    # Schedule methods
    def get_last_5_events_by_team(self, team_id: int) -> Dict[str, Any]:
        """
        Get the last 5 events for a team (limited to home team for free tier).

        :param team_id: Team ID, e.g. 133602
        :return: Last 5 events
        """
        return self._schedule_service.get_last_5_events_by_team(team_id)

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
        return self._schedule_service.get_events_by_round(league_id, round_number, season)

    def get_events_in_league_by_season(self, league_id: int, season: str) -> Dict[str, Any]:
        """
        Get all events in a league for a season (Free tier limited to 100 events).

        :param league_id: League ID, e.g. 4328
        :param season: Season, e.g. '2014-2015'
        :return: Events in the league for the season
        """
        return self._schedule_service.get_events_in_league_by_season(league_id, season)
