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
        all_rounds_data = []

        for round_num in range(start_round, end_round + 1):
            print(f"Retrieving data for round {round_num}")

            try:
                round_data = self.api_client.get_events_by_round(league_id, round_num, season)
                if round_data and round_data.get('events'):
                    matches = round_data['events']
                    all_rounds_data.extend(matches)
                    print(f'Round {round_num}: retrieved {len(matches)} matches.')
                else:
                    print(f'Round {round_num}: no data was found.')
            except Exception as e:
                print(f'Error while retrieving data for round {round_num}: {e}')

            sleep(1)

        return all_rounds_data

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
        Save data to JSON file.

        :param data: Variable with the data to be saved.
        :param output_path: Optional override for output path from config.
        :param output_file: Optional override for output filename from config.
        """
        storage_config = self.config.get_output_settings()

        final_path = output_path or storage_config['output_path']
        final_file = output_file or storage_config['default_file']

        self._make_directory(final_path)

        output_file_path = os.path.join(final_path, final_file)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f'Data saved to: {output_file_path}')

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
        if all_rounds_data and save_data:
            self._save_json_file(all_rounds_data, output_path, output_file)
        return all_rounds_data
