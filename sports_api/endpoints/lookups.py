from sports_api.endpoints.decorators import premium_required


class Lookups:
    @premium_required
    def lookup_league_details_by_id(self, league_id: int) -> str:
        """
        League Details by league's Id.

        :param league_id: League's id, e.g. 4346.
        :return: str
        """
        return f'lookupleague.php?id={league_id}'

    @premium_required
    def lookup_team_details_by_id(self, team_id: int) -> str:
        """
        Team Details by team's Id.

        :param team_id: Team's id, e.g. 133604.
        :return: str
        """
        return f'lookupteam.php?id={team_id}'

    @staticmethod
    def lookup_player_details_by_id(player_id: int) -> str:
        """
        Player Details by player's Id.

        :param player_id: Player's id, e.g. 34145937.
        :return: str
        """
        return f'lookupplayer.php?id={player_id}'

    @staticmethod
    def lookup_venue_details_by_id(venue_id: int) -> str:
        """
        Venue Details by venue's Id.

        :param venue_id: Venue's id, e.g. 16163.
        :return: str
        """
        return f'lookupvenue.php?id={venue_id}'

    @premium_required
    def lookup_event_details_by_id(self, event_id: int) -> str:
        """
        Event Details by event's Id.

        :param event_id: Event's id, e.g. 441613.
        :return: str
        """
        return f'lookupevent.php?id={event_id}'

    @premium_required
    def lookup_event_statistics_by_id(self, event_id: int) -> str:
        """
        Event Statistics by event's Id.

        :param event_id: Event's id, e.g. 1032723.
        :return: str
        """
        return f'lookupeventstats.php?id={event_id}'

    @premium_required
    def lookup_event_lineup_by_id(self, event_id: int) -> str:
        """
        Event Lineup by event's Id.

        :param event_id: Event's id, e.g. 1032723.
        :return: str
        """
        return f'lookuplineup.php?id={event_id}'

    @premium_required
    def lookup_event_timeline_by_id(self, event_id: int) -> str:
        """
        List timeline for events by event ID.

        :param event_id: Event's id, e.g. 1032718.
        :return: str
        """
        return f'lookuptimeline.php?id={event_id}'

    @staticmethod
    def lookup_player_honours_by_id(player_id: int) -> str:
        """
        Player's Honours by Player Id.

        :param player_id: Player's id, e.g. 34147178.
        :return: str
        """
        return f'lookuphonours.php?id={player_id}'

    @staticmethod
    def lookup_player_milestones_by_id(player_id: int) -> str:
        """
        Player Milestones by Player Id.

        :param player_id: Player's id, e.g. 34161397.
        :return: str
        """
        return f'lookupmilestones.php?id={player_id}'

    @staticmethod
    def lookup_player_former_teams_by_id(player_id: int) -> str:
        """
        Player Former Teams by Player Id.

        :param player_id: Player's id, e.g. 34147178.
        :return: str
        """
        return f'lookupformerteams.php?id={player_id}'

    @staticmethod
    def lookup_player_contracts_by_id(player_id: int) -> str:
        """
        Player Contracts by Player Id.

        :param player_id: Player's id, e.g. 34147178.
        :return: str
        """
        return f'lookupcontracts.php?id={player_id}'

    @staticmethod
    def lookup_event_player_results_by_event_id(event_id: int) -> str:
        """
        Event Player Results by Event Id.

        :param event_id: Event's id, e.g. 652890.
        :return: str
        """
        return f'eventresults.php?id={event_id}'

    @premium_required
    def lookup_event_tv_by_id(self, event_id: int) -> str:
        """
        Event TV by Event Id.

        :param event_id: Event's id, e.g. 584911.
        :return: str
        """
        return f'lookuptv.php?id={event_id}'

    @staticmethod
    def lookup_table_by_league_and_season(league_id: int, season: str) -> str:
        """
        Lookup Table by League ID and Season.

        :param league_id: League's id, e.g. 4328.
        :param season: Season, e.g. '2020-2021'.
        :return: str
        """
        return f'lookuptable.php?l={league_id}&s={season}'

    @staticmethod
    def lookup_equipment_by_team_id(team_id: int) -> str:
        """
        Lookup Equipment (kits) by Team ID.

        :param team_id: Team's id, e.g. 133597.
        :return: str
        """
        return f'lookupequipment.php?id={team_id}'
