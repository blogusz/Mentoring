import json
import os
from time import sleep
from typing import Any

from sports_api.config import Config
from sports_api import ApiClient


class DataScraper:
    def __init__(self, config: Config = None, api_client: ApiClient = None):
        self.config = config
        self.api_client = api_client or (ApiClient(config) if config else None)

    def _retrieve_all_rounds(self, league_id: int, season: str, start_round: int, end_round: int) -> list[Any]:
        """
        :param league_id: League ID (e.g. 4335 for Spanish La Liga).
        :param season: Season (e.g. '2024-2025').
        :param start_round: Number of the first round to retrieve.
        :param end_round: Number of the last round to retrieve (inclusive).
        :return:
        """
        all_matches = []

        for round_number in range(start_round, end_round + 1):
            print(f'Retrieving data for round {round_number}')

            try:
                data = self.api_client.get_events_by_round(league_id, round_number, season)
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
    def _make_directory(path: str):
        """
        :param path: Path where the folder will be created.
        :return: bool
        """
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                return True
            except OSError as e:
                print(f'Error while making directory {path}: {e}')
                return False

    def _save_json_file(self, data: list[Any], output_path: str = None, output_file: str = None) -> None:
        """
        Save data to JSON file using configuration settings.

        :param data: Variable with the data to be saved
        :param output_path: Optional override for output path from config
        :param output_file: Optional override for output filename from config
        """
        if not self.config:
            raise ValueError("Config object is required for saving data")

        storage_config = self.config.get_output_settings()

        final_path = output_path or storage_config['output_path']
        final_file = output_file or storage_config['default_file']

        self._make_directory(final_path)

        output_file_path = os.path.join(final_path, final_file)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f'Data saved to directory: {output_file_path}')

    def scrape_all_rounds(self, league_id: int, season: str, start_round: int = None, end_round: int = None,
                          output_path: str = None, output_file: str = None, save_data=False) -> list[Any]:
        """
        The function retrieves data from the API for consecutive rounds (from start_round to end_round inclusive)
        for the specified season and league, and then saves all the returned data to a single JSON file.

        :param league_id: League ID (e.g. 4335 for Spanish La Liga)
        :param season: Season (e.g. '2024-2025')
        :param start_round: Number of the first round to retrieve
        :param end_round: Number of the last round to retrieve (inclusive)
        :param output_path: Optional override for output path from config
        :param output_file: Optional override for output filename from config
        :param save_data: Whether the data is to be saved to disk
        :rtype: list[Any]
        """
        all_rounds_data = self._retrieve_all_rounds(league_id, season, start_round, end_round)
        if save_data:
            self._save_json_file(all_rounds_data, output_path, output_file)
        return all_rounds_data
