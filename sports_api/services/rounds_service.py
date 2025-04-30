from typing import Any, Optional

from sports_api.config import Config
from sports_api.data_scraper import DataScraper
from sports_api.services.base_service import BaseService


class RoundsService(BaseService):
    """
    Service class for handling round-related operations.
    This is an internal class not meant to be used directly by users.
    """

    def __init__(self, config: Config, data_scraper: Optional[DataScraper] = None):
        super().__init__(config)
        self.data_scraper = data_scraper or DataScraper(config)

    def get_all_rounds(self, league_id: int, season: str, start_round: int, end_round: int,
                       output_path: str = 'retrieved_data/raw/', output_file: str = None,
                       save_data: bool = False) -> list[Any]:
        """
        The function retrieves data from the API for consecutive rounds (from start_round to end_round inclusive)
        for the specified season and league, and then saves all the returned data to a single JSON file.

        :param league_id: League ID (e.g. 4335 for Spanish La Liga).
        :param season: Season (e.g. '2024-2025').
        :param start_round: Number of the first round to retrieve.
        :param end_round: Number of the last round to retrieve (inclusive).
        :param output_path: Path where the data will be saved.
        :param output_file: Name of the file where the data will be saved.
        :param save_data: Whether the data is to be saved to disk.
        :rtype: list[Any]
        """
        all_rounds = self.data_scraper.scrape_all_rounds(
            self.config, league_id, season, start_round, end_round,
            output_path, output_file, save_data
        )
        return all_rounds
