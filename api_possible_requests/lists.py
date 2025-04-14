from .decorators import premium_required


class Lists:
    @premium_required
    def list_all_sports(self) -> str:
        """
        List all sports.

        :return: str
        """
        return 'all_sports.php'

    @staticmethod
    def list_all_leagues() -> str:
        """
        List all leagues (limited 50 on free tier).

        :return: str
        """
        return 'all_leagues.php'

    @staticmethod
    def list_all_countries() -> str:
        """
        List all countries.

        :return: str
        """
        return 'all_countries.php'

    @staticmethod
    def list_all_leagues_in_country(country: str, sport: str = None) -> str:
        """
        List all Leagues in a country (limited 50 on free tier).

        :param country: Country's name, e.g. 'England' .
        :param sport: (optional) Sport's name, e.g 'Soccer'.
        :return: str

        \n Example 1: search_all_leagues.php?c=England
        \n Example 2: search_all_leagues.php?c=England&s=Soccer
        """
        if sport:
            return f'search_all_leagues.php?c={country}&s={sport}'
        else:
            return f'search_all_leagues.php?c={country}'

    @staticmethod
    def list_all_seasons_in_league(id: int, poster: int = None, badge: int = None) -> str:
        """
        List all Seasons in a League (or show posters and badges from seasons).

        :param id: League's id, e.g. '4328' .
        :param poster: (optional) Poster's id, e.g. '1'.
        :param badge: (optional) Badge's id, e.g. '1'.
        :return: str

        \n Example: search_all_leagues.php?c=England&s=Soccer
        """
        if poster:
            return f'search_all_seasons.php?id={id}&poster={poster}'
        elif badge:
            return f'search_all_seasons.php?id={id}&badge={badge}'
        else:
            return f'search_all_seasons.php?id={id}'

    @staticmethod
    def list_all_teams_in_league(league_name: str, sport: str = None, country: str = None) -> str:
        """
        List all Teams in a League.

        :param league_name:
        :param sport: (optional) Sport's name, e.g 'Soccer'.
        :param country: (optional) Country's name, e.g. 'Spain'.
        :return: str

        \n Example 1: search_all_teams.php?l=English%20Premier%20League
        \n Example 2: search_all_teams.php?s=Soccer&c=Spain
        """

        if sport and country:
            return f'search_all_teams.php?s={sport}&c={country}'
        else:
            return f'search_all_teams.php?l={league_name}'

    @premium_required
    def list_all_teams_details_in_league_by_league_id(self, league_id: int) -> str:
        """
        List All teams details in a league by Id.

        :param league_id: League's id, e.g. 4328.
        :return: str
        """
        return f'lookup_all_teams.php?id={league_id}'

    @premium_required
    def list_all_players_in_team_by_team_id(self, team_id: int) -> str:
        """
        List All players in a team by team's Id.

        :param team_id: Team's id, e.g. 133604.
        :return: str
        """
        return f'lookup_all_players.php?id={team_id}'

    @staticmethod
    def list_all_users_loved_teams_and_players(username: str) -> str:
        """
        List all users loved teams and players.

        :param username: User's nickname, e.g. 'zag'.
        :return: str
        """
        return f'searchloves.php?u={username}'
