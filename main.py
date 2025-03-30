import os
import json
import requests
from dotenv import load_dotenv

from api_possible_requests.lists import list_all_sports, list_all_leagues, list_all_countries, \
    list_all_leagues_in_country, list_all_seasons_in_league, list_all_teams_in_league, \
    list_all_teams_details_in_league_by_league_id, list_all_players_in_team_by_team_id, \
    list_all_users_loved_teams_and_players
from api_possible_requests.schedules import events_next_5_by_team_id, events_next_25_by_league_id, \
    events_last_5_by_team_id, events_last_15_by_league_id, events_by_round, events_on_day, tv_events_on_day, \
    events_in_season_by_league
from api_possible_requests.searches import search_team_by_name, search_team_by_shortcode, search_player_by_name, \
    search_all_players_from_team, search_event_by_event_name, search_event_by_file_name, search_venue_by_name
from api_possible_requests.lookups import lookup_league_details_by_id, lookup_team_details_by_id, \
    lookup_player_details_by_id, lookup_venue_details_by_id, lookup_event_details_by_id, lookup_event_statistics_by_id, \
    lookup_event_lineup_by_id, lookup_event_timeline_by_id, lookup_player_honours_by_id, lookup_player_milestones_by_id, \
    lookup_player_former_teams_by_id, lookup_player_contracts_by_id, lookup_event_player_results_by_id, \
    lookup_event_tv_by_id, lookup_table_by_league_and_season, lookup_equipment_by_team_id


def test_endpoint(function, *args, **kwargs):
    """
    Function for testing endpoints.
    """
    # if function.is_premium:
    #     print(f'Function {function.__name__} requires premium API key.')
    if getattr(function, "is_premium", False):
        print(f'Function {function.__name__} requires premium API key.')

    endpoint = function(*args, **kwargs)
    request = f'{base_url}/{api_key}/{endpoint}'
    print(f'Function {function.__name__} with arguments {args} {kwargs}')
    print(f'Built request: {request}')
    response = requests.get(request)
    status = response.status_code
    if status == 200:
        data = response.json()
        # print(json.dumps(data, indent=4, ensure_ascii=False))
        print(json.dumps(data, indent=4))
    else:
        print(f'Error, status code: {status}')
        raise E


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY') or 3
    base_url = f'https://www.thesportsdb.com/api/v1/json'

    # search functions
    test_endpoint(search_team_by_name, 'Real_Madrid')
    test_endpoint(search_team_by_shortcode, 'ARS')
    test_endpoint(search_player_by_name, 'Ronaldo')
    test_endpoint(search_all_players_from_team, team='Real_Madrid')
    test_endpoint(search_event_by_event_name, 'Real_Madrid_vs_Barcelona')
    test_endpoint(search_event_by_file_name, 'English_Premier_League_2015-04-26_Arsenal_vs_Chelsea')
    test_endpoint(search_venue_by_name, 'Wembley')

    # lookup functions
    test_endpoint(lookup_league_details_by_id, 4346)
    test_endpoint(lookup_team_details_by_id, 133604)
    test_endpoint(lookup_player_details_by_id, 34145937)
    test_endpoint(lookup_venue_details_by_id, 16163)
    test_endpoint(lookup_event_details_by_id, 441613)
    test_endpoint(lookup_event_statistics_by_id, 1032723)
    test_endpoint(lookup_event_lineup_by_id, 1032723)
    test_endpoint(lookup_event_timeline_by_id, 1032718)
    test_endpoint(lookup_player_honours_by_id, 34147178)
    test_endpoint(lookup_player_milestones_by_id, 34161397)
    test_endpoint(lookup_player_former_teams_by_id, 34147178)
    test_endpoint(lookup_player_contracts_by_id, 34147178)
    test_endpoint(lookup_event_player_results_by_id, 652890)
    test_endpoint(lookup_event_tv_by_id, 584911)
    test_endpoint(lookup_table_by_league_and_season, 4328, '2020-2021')
    test_endpoint(lookup_equipment_by_team_id, 133597)

    # list functions
    test_endpoint(list_all_sports)
    test_endpoint(list_all_leagues)
    test_endpoint(list_all_countries)

    test_endpoint(list_all_leagues_in_country, 'England')
    test_endpoint(list_all_leagues_in_country, 'England', sport='Soccer')

    test_endpoint(list_all_seasons_in_league, 4328)
    test_endpoint(list_all_seasons_in_league, 4328, poster=1)

    test_endpoint(list_all_teams_in_league, 'English Premier League')
    test_endpoint(list_all_teams_in_league, 'English Premier League', sport='Soccer', country='Spain')

    test_endpoint(list_all_teams_details_in_league_by_league_id, 4328)
    test_endpoint(list_all_players_in_team_by_team_id, 133604)
    test_endpoint(list_all_users_loved_teams_and_players, 'zag')

    # schedule functions
    test_endpoint(events_next_5_by_team_id, 133602)
    test_endpoint(events_next_25_by_league_id, 4328)
    test_endpoint(events_last_5_by_team_id, 133602)
    test_endpoint(events_last_15_by_league_id, 4328)
    test_endpoint(events_by_round, 4328, 38, '2014-2015')

    test_endpoint(events_on_day, '2014-10-10')
    test_endpoint(events_on_day, '2014-10-10', sport='Soccer')
    test_endpoint(events_on_day, '2014-10-10', league='4356')
    test_endpoint(events_on_day, '2014-10-10', league='Australian_A-League')

    test_endpoint(tv_events_on_day, day='2018-07-07')
    test_endpoint(tv_events_on_day, day='2018-07-07', sport='Fighting')
    test_endpoint(tv_events_on_day, day='2019-09-28', station_country='United Kingdom', sport='Cycling')
    test_endpoint(tv_events_on_day, channel='Peacock_Premium')

    test_endpoint(events_in_season_by_league, 4328, '2014-2015')
