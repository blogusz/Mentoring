from sports_api.endpoints.decorators import premium_required


class Schedules:
    @premium_required
    def events_next_5_by_team_id(self, team_id: int) -> str:
        """
        Next 5 Events by Team Id.

        :param team_id: Team's id, e.g. 133602.
        :return: str
        """
        return f'eventsnext.php?id={team_id}'

    @premium_required
    def events_next_25_by_league_id(self, league_id: int) -> str:
        """
        Next 25 Events by League Id.

        :param league_id: League's id, e.g. 4328.
        :return: str
        """
        return f'eventsnextleague.php?id={league_id}'

    @staticmethod
    def events_last_5_by_team_id(team_id: int) -> str:
        """
        Last 5 Events by Team Id (Limited to home team for free tier).

        :param team_id: Team's id, e.g. 133602.
        :return: str
        """
        return f'eventslast.php?id={team_id}'

    @premium_required
    def events_last_15_by_league_id(self, league_id: int) -> str:
        """
        Last 15 Events by League Id.

        :param league_id: League's id, e.g. 4328.
        :return: str
        """
        return f'eventspastleague.php?id={league_id}'

    @staticmethod
    def events_by_round(league_id: int, round: int, season: str) -> str:
        """
        Events in a specific round by league id/round/season.

        \n Note: Special round numbers:
          - Round 125 = Quarter-Final
          - Round 150 = Semi-Final
          - Round 160 = Playoff
          - Round 170 = Playoff Semi-Final
          - Round 180 = Playoff Final
          - Round 200 = Final
          - Round 500 = Pre-Season

        :param league_id: League's id, e.g. 4328.
        :param round: Round number, e.g. 38.
        :param season: Season string, e.g. '2014-2015'.
        :return: str
        """
        return f'eventsround.php?id={league_id}&r={round}&s={season}'

    @premium_required
    def events_on_day(self, day: str, sport: str = None, league: str = None) -> str:
        """
        Events on a specific day.

        Examples:
          \n eventsday.php?d=2014-10-10
          \n eventsday.php?d=2014-10-10&s=Soccer
          \n eventsday.php?d=2014-10-10&l=4356
          \n eventsday.php?d=2014-10-10&l=Australian_A-League

        :param day: Date in YYYY-MM-DD format, e.g. '2014-10-10'.
        :param sport: (optional) Sport's name, e.g. 'Soccer'.
        :param league: (optional) League's id or name, e.g. '4356' or 'Australian_A-League'.
        :return: str
        """
        params = [f"d={day}"]
        if sport:
            params.append(f"s={sport}")
        if league:
            params.append(f"l={league}")
        return "eventsday.php?" + "&".join(params)

    @premium_required
    def tv_events_on_day(self, day: str = None, sport: str = None, station_country: str = None,
                         channel: str = None) -> str:
        """
        TV Events on a day (By Sport/Date/TV Station Country).

        Examples:
          \n eventstv.php?d=2018-07-07
          \n eventstv.php?d=2018-07-07&s=Fighting
          \n eventstv.php?d=2019-09-28&a=United%20Kingdom&s=Cycling
          \n eventstv.php?c=Peacock_Premium
        :param day: (optional) Date in YYYY-MM-DD format.
        :param sport: (optional) Sport's name.
        :param station_country: (optional) TV Station Country (query parameter 'a').
        :param channel: (optional) Channel name (query parameter 'c').
        :return: str
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
        return "eventstv.php?" + "&".join(params)

    @staticmethod
    def events_in_league_by_season(league_id: int, season: str) -> str:
        """
        All events in a specific league by season (Free tier limited to 100 events).

        :param league_id: League's id, e.g. 4328.
        :param season: Season string, e.g. '2014-2015'.
        :return: str
        """
        return f'eventsseason.php?id={league_id}&s={season}'
