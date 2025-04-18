import json
import requests

from api_possible_requests.searches import Searches
from api_possible_requests.lists import Lists
from api_possible_requests.lookups import Lookups
from api_possible_requests.schedules import Schedules

from config import Config


def test_endpoint(function, *args, **kwargs):
    """
    Function for testing endpoints.
    """

    if getattr(function, 'is_premium', False):
        print(f'Function \'{function.__name__}\' requires premium API key.')
        return

    endpoint = function(*args, **kwargs)
    request = f'{base_url}/{api_key}/{endpoint}'
    print(f'Function {function.__name__} with arguments {args} {kwargs}')
    print(f'Built request: {request}')
    response = requests.get(request)
    status = response.status_code
    if status == 200:
        data = response.json()
        print(json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print(f'Error, status code: {status}')


if __name__ == '__main__':
    config = Config()
    api_key, base_url = config.get_credentials()

    # search functions
    searches = Searches()
    test_endpoint(searches.search_team_by_name, 'Real_Madrid')
    test_endpoint(searches.search_team_by_shortcode, 'ARS')
    test_endpoint(searches.search_player_by_name, 'Ronaldo')
    test_endpoint(searches.search_event_by_event_name, 'Real_Madrid_vs_Barcelona')
    test_endpoint(searches.search_event_by_file_name, 'English_Premier_League_2015-04-26_Arsenal_vs_Chelsea')
    test_endpoint(searches.search_venue_by_name, 'Wembley')

    # list functions
    lists = Lists()
    test_endpoint(lists.list_all_leagues)
    test_endpoint(lists.list_all_countries)

    test_endpoint(lists.list_all_leagues_in_country, 'England')
    test_endpoint(lists.list_all_leagues_in_country, 'England', sport='Soccer')

    test_endpoint(lists.list_all_seasons_in_league, 4328)
    test_endpoint(lists.list_all_seasons_in_league, 4328, poster=1)
    test_endpoint(lists.list_all_seasons_in_league, 4328, badge=1)

    test_endpoint(lists.list_all_teams_in_league, 'English Premier League')
    test_endpoint(lists.list_all_teams_in_league, 'English Premier League', sport='Soccer', country='Spain')
    test_endpoint(lists.list_all_users_loved_teams_and_players, 'zag')

    # lookup functions
    lookups = Lookups()
    test_endpoint(lookups.lookup_player_details_by_id, 34145937)
    test_endpoint(lookups.lookup_venue_details_by_id, 16163)
    test_endpoint(lookups.lookup_player_honours_by_id, 34147178)
    test_endpoint(lookups.lookup_player_milestones_by_id, 34161396)
    test_endpoint(lookups.lookup_player_former_teams_by_id, 34147178)
    test_endpoint(lookups.lookup_player_contracts_by_id, 34147178)
    test_endpoint(lookups.lookup_event_player_results_by_event_id, 528358)  # doesn't work for chosen event_ids
    test_endpoint(lookups.lookup_table_by_league_and_season, 4335, '2024-2025')
    test_endpoint(lookups.lookup_equipment_by_team_id, 133597)

    # schedule functions
    schedules = Schedules()
    test_endpoint(schedules.events_last_5_by_team_id, 133738)
    test_endpoint(schedules.events_by_round, 4335, 1, '2024-2025')
    test_endpoint(schedules.events_in_league_by_season, 4335, '2024-2025')
