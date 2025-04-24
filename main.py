from pprint import pprint

from sports_api.api_client import ApiClient

if __name__ == '__main__':
    api_client = ApiClient()

    # Get all rounds for a league
    rounds_data = api_client.get_all_rounds(
        league_id=4335,  # Spanish La Liga
        season='2024-2025',
        start_round=1,
        end_round=5,
        output_file='data.json',
        save_data=True
    )
    pprint(rounds_data)

    # Example of using other API methods
    # leagues = api_client.get_all_leagues()
    # pprint(leagues)
    # team = api_client.search_team("Barcelona")
    # pprint(team)
