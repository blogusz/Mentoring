import json
import os
import requests
from dotenv import load_dotenv

from api_possible_requests.lists import list_all_leagues, list_all_countries, list_all_leagues_in_country, \
    list_all_seasons_in_league, list_all_teams_in_league, list_all_users_loved_teams_and_players
from api_possible_requests.lookups import lookup_player_details_by_id, lookup_venue_details_by_id, \
    lookup_player_honours_by_id, lookup_player_milestones_by_id, lookup_player_former_teams_by_id, \
    lookup_player_contracts_by_id, lookup_event_player_results_by_event_id, lookup_table_by_league_and_season, \
    lookup_equipment_by_team_id
from api_possible_requests.schedules import events_last_5_by_team_id, events_by_round, events_in_league_by_season
from api_possible_requests.searches import search_team_by_name, search_team_by_shortcode, search_player_by_name, \
    search_event_by_event_name, search_event_by_file_name, search_venue_by_name


def test_endpoint(function, *args, **kwargs):
    """
    Function for testing endpoints.
    """

    if getattr(function, "is_premium", False):
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
    load_dotenv()
    api_key = os.getenv('API_KEY') or 3
    base_url = f'https://www.thesportsdb.com/api/v1/json'

    # search functions
    test_endpoint(search_team_by_name, 'Real_Madrid')
    test_endpoint(search_team_by_shortcode, 'ARS')
    test_endpoint(search_player_by_name, 'Ronaldo')
    test_endpoint(search_event_by_event_name, 'Real_Madrid_vs_Barcelona')
    test_endpoint(search_event_by_file_name, 'English_Premier_League_2015-04-26_Arsenal_vs_Chelsea')
    test_endpoint(search_venue_by_name, 'Wembley')

    # list functions
    test_endpoint(list_all_leagues)
    test_endpoint(list_all_countries)

    test_endpoint(list_all_leagues_in_country, 'England')
    test_endpoint(list_all_leagues_in_country, 'England', sport='Soccer')

    test_endpoint(list_all_seasons_in_league, 4328)
    test_endpoint(list_all_seasons_in_league, 4328, poster=1)
    test_endpoint(list_all_seasons_in_league, 4328, badge=1)

    test_endpoint(list_all_teams_in_league, 'English Premier League')
    test_endpoint(list_all_teams_in_league, 'English Premier League', sport='Soccer', country='Spain')
    test_endpoint(list_all_users_loved_teams_and_players, 'zag')

    # lookup functions
    test_endpoint(lookup_player_details_by_id, 34145937)
    test_endpoint(lookup_venue_details_by_id, 16163)
    test_endpoint(lookup_player_honours_by_id, 34147178)
    test_endpoint(lookup_player_milestones_by_id, 34161396)
    test_endpoint(lookup_player_former_teams_by_id, 34147178)
    test_endpoint(lookup_player_contracts_by_id, 34147178)
    test_endpoint(lookup_event_player_results_by_event_id, 652890)
    test_endpoint(lookup_table_by_league_and_season, 4328, '2020-2021')
    test_endpoint(lookup_equipment_by_team_id, 133597)

    # schedule functions
    test_endpoint(events_last_5_by_team_id, 133602)
    test_endpoint(events_by_round, 4328, 38, '2014-2015')
    test_endpoint(events_in_league_by_season, 4328, '2014-2015')
