from .decorators import premium_required


def search_team_by_name(name: str) -> str:
    """
    Search for team by name.

    :param name: Team's name, e.g. 'Arsenal'.
    :return: str
    """
    return f'searchteams.php?t={name}'


def search_team_by_shortcode(shortcode: str) -> str:
    """
    Search for team short code.

    :param shortcode: Short code for team's name, e.g. 'ARS' for Arsenal.
    :return: str
    """
    return f'searchteams.php?t={shortcode}'


def search_player_by_name(name: str) -> str:
    """
    Search for players by name.

    :param name: Player's name, surname or full name, e.g. 'Danny', 'Welbeck', 'Danny_Welbeck'.
    :return: str
    """
    return f'searchplayers.php?p={name}'


@premium_required
def search_all_players_from_team(team: str) -> str:
    """
    Search for all players from team.

    :param team: Team's name, e.g. 'Arsenal'.
    :return: str
    """
    return f'searchplayers.php?t={team}'


def search_event_by_event_name(event_name: str) -> str:
    """
    Search for event by event's name.

    :param event_name: Event's name, e.g. 'Arsenal_vs_Chelsea', 'Arsenal_vs_Chelsea&s=2016-2017'.
    :return: str
    """
    return f'searchevents.php?e={event_name}'


def search_event_by_file_name(file_name: str) -> str:
    """
    Search for event by event's file name.

    :param file_name: Event's file name, e.g. 'English_Premier_League_2015-04-26_Arsenal_vs_Chelsea'.
    :return: str
    """
    return f'searchfilename.php?e={file_name}'


def search_venue_by_name(name: str) -> str:
    """
    Search for Venue by name.

    :param name: Venue's name, e.g. 'Wembley'.
    :return: str
    """
    return f'searchvenues.php?t={name}'
