import json
import os
from time import sleep
from typing import Any, Dict, Callable, Optional

from sports_api.config import Config
from sports_api import ApiClient
from sports_api.utils.file_utils import save_json_file


class DataScraper:
    """
        Responsible for scraping data from the API and saving it to disk.
    """

    def __init__(self, config: Config = None, api_client: ApiClient = None):
        self.config = config
        self.api_client = api_client or (ApiClient(config) if config else None)

    def scrape_data(self, scraper_func: Callable, save_data: bool = False,
                    output_path: str = None, output_file: str = None, **kwargs) -> Any:
        """
        Generic method to scrape data using the provided scraper function.

        :param scraper_func: Function that will be called to retrieve data
        :param save_data: Whether to save the data to disk
        :param output_path: Optional override for output path
        :param output_file: Optional override for output filename
        :param kwargs: Additional arguments to pass to the scraper function
        :return: The scraped data
        """
        data = scraper_func(**kwargs)

        if data and save_data and self.config:
            storage_config = self.config.get_output_settings()
            final_path = output_path or storage_config['output_path']
            final_file = output_file or storage_config['default_file']
            save_json_file(data, final_path, final_file)

        return data

    def _retrieve_all_rounds(self, league_id: int, season: str, start_round: int, end_round: int) -> list[Any]:
        """
        Retrieve data for all rounds in the specified range.

        :param league_id: League ID (e.g. 4335 for Spanish La Liga)
        :param season: Season (e.g. '2024-2025')
        :param start_round: Number of the first round to retrieve
        :param end_round: Number of the last round to retrieve (inclusive)
        :return: List of all matches from the specified rounds
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

    def scrape_all_rounds(self, league_id: int, season: str, start_round: int = 1, end_round: int = 38,
                          output_path: str = None, output_file: str = None, save_data: bool = False) -> list[Any]:
        """
        Scrape data for consecutive rounds for the specified season and league.

        :param league_id: League ID (e.g. 4335 for Spanish La Liga)
        :param season: Season (e.g. '2024-2025')
        :param start_round: Number of the first round to retrieve
        :param end_round: Number of the last round to retrieve (inclusive)
        :param output_path: Optional override for output path from config
        :param output_file: Optional override for output filename from config
        :param save_data: Whether the data is to be saved to disk
        :return: List of round data
        """
        return self.scrape_data(
            scraper_func=self._retrieve_all_rounds,
            save_data=save_data,
            output_path=output_path,
            output_file=output_file,
            league_id=league_id,
            season=season,
            start_round=start_round,
            end_round=end_round
        )
