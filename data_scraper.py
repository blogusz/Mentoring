import os
from typing import Any
import requests
import json
from time import sleep


class DataScraper:
    @staticmethod
    def retrieve_all_rounds(config, league_id, season, start_round, end_round):
        from api_possible_requests.schedules import events_by_round

        api_key, base_url = config.get_credentials()
        all_matches = []

        for round_number in range(start_round, end_round + 1):
            endpoint = events_by_round(league_id, round_number, season)
            url = f'{base_url}/{api_key}/{endpoint}'
            print(f'Retrieving data for round {round_number}: {url}')

            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                if data and data.get('events'):
                    matches = data['events']
                    all_matches.extend(matches)
                    print(f'Round {round_number}: retrieved {len(matches)} matches.')
                else:
                    print(f'Round {round_number}: no data was found.')
            except Exception as e:
                print(f'Error while retrieving data for round {round_number}: {e}')

            sleep(1)

        return all_matches

    @staticmethod
    def make_directory(path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                return True
            except OSError as e:
                print(f'Error while making directory {path}: {e}')
                return False

    def save_json_file(self, data: list[Any], output_path: str = 'retrieved_data/raw/',
                       output_file: str = 'data.json') -> None:
        """
        :param output_path: Path where the data will be saved.
        :param output_file: Name of the file where the data will be saved.
        :param data: Variable with the data to be saved.
        """
        self.make_directory(output_path)

        output_file_path = os.path.join(output_path, output_file)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f'Data saved to directory: {output_file_path}')

    def scrape_all_rounds(self, config, league_id: int, season: str, start_round: int, end_round: int,
                          output_path: str = '',
                          output_file: str = None, save_data=False) -> list[Any]:
        """
        The function retrieves data from the API for consecutive rounds (from start_round to end_round inclusive) for the specified season and league, and then saves all the returned data to a single JSON file.

        :param config: Config class object containing the API key.
        :param league_id: League ID (e.g. 4335 for Spanish La Liga).
        :param season: Season (e.g. '2024-2025').
        :param start_round: Number of the first round to retrieve.
        :param end_round: Number of the last round to retrieve (inclusive).
        :param output_path: Path where the data will be saved.
        :param output_file: Name of the file where the data will be saved.
        :param save_data: Whether the data is to be saved to disk.
        :rtype: list[Any]
        """

        all_rounds_data = self.retrieve_all_rounds(config, league_id, season, start_round, end_round)
        if save_data:
            self.save_json_file(all_rounds_data, output_path, output_file)
        return all_rounds_data
