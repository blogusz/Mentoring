from time import sleep
from typing import Any, Callable

from sports_api import ApiClient
from sports_api.config import Config
from sports_api.storage.file_storage import FileStorage
from sports_api.storage.storage_interface import StorageInterface
from sports_api.storage.db_storage import DatabaseStorage
from sports_api.utils.datascraper_utils import league_id_to_name


class DataScraper:
    """
    Responsible for scraping data from the API and saving it to disk.
    """

    def __init__(self, config: Config = None, api_client: Any = None, storage: StorageInterface = None,
                 use_db_storage: bool = True):
        """
        Initialize the data scraper.

        :param config: Config object
        :param api_client: Any API client that provides data retrieval methods
        :param storage: StorageInterface object to use for saving data (defaults to FileStorage)
        :param use_db_storage: Whether to use database storage in addition to file storage
        """
        self.config = config
        self.api_client = api_client or (ApiClient(config) if config else None)

        if not self.api_client:
            raise ValueError("Either valid config or api_client must be provided.")

        if storage:
            self.storage = storage
        else:
            self.storage = FileStorage(config)

        self.db_storage = None
        if use_db_storage and config and 'database' in config.config_data:
            self.db_storage = DatabaseStorage(config)

    def scrape_data(self, scraper_func: Callable, save_data: bool = False, data_type: str = None, **kwargs) -> Any:
        """
        Generic method to scrape data using the provided scraper function.

        :param scraper_func: Function that will be called to retrieve data
        :param save_data: Whether to save the data to disk
        :param data_type: Type of data for automatic file naming
        :param kwargs: Additional arguments to pass to the scraper function and storage
        :return: The scraped data
        """
        data = scraper_func(**kwargs)

        if data and save_data and self.storage:
            self.storage.save(data, data_type, **kwargs)

        return data

    def _retrieve_all_rounds(self, league_id: int, season: str, start_round: int, end_round: int,
                             save_individual_rounds: bool = False) -> list[Any]:
        """
        Retrieve data for all rounds in the specified range.

        :param league_id: League ID (e.g. 4335 for Spanish La Liga)
        :param season: Season (e.g. '2024-2025')
        :param start_round: Number of the first round to retrieve
        :param end_round: Number of the last round to retrieve (inclusive)
        :param save_individual_rounds: Whether to save each round to a separate file
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

                    if save_individual_rounds:
                        if self.storage:
                            self.storage.save(
                                data=matches,
                                data_type="rounds",
                                league_id=league_id,
                                season=season,
                                round_num=round_num
                            )
                        else:
                            print("No storage implementation provided, skipping individual round save.")
                else:
                    print(f'Round {round_num}: no data was found.')
            except Exception as e:
                print(f'Error while retrieving data for round {round_num}: {e}')

            sleep(1)

        return all_rounds_data

    def scrape_all_rounds(self, league_id: int, season: str, start_round: int = 1, end_round: int = 38,
                          output_path: str = None, output_file: str = None, save_all_rounds: bool = False,
                          save_individual_rounds: bool = False) -> list[Any]:
        """
        Scrape data for consecutive rounds for the specified season and league.

        :param league_id: League ID (e.g. 4335 for Spanish La Liga)
        :param season: Season (e.g. '2024-2025')
        :param start_round: Number of the first round to retrieve
        :param end_round: Number of the last round to retrieve (inclusive)
        :param output_path: Optional override for output path from config
        :param output_file: Optional override for output filename from config
        :param save_all_rounds: Whether to save the data to disk into a single file
        :param save_individual_rounds: Whether to save each round to a separate file
        :return: List of round data
        """
        return self.scrape_data(
            scraper_func=self._retrieve_all_rounds,
            save_data=save_all_rounds,
            # output_path=output_path,
            # output_file=output_file,
            data_type="rounds",
            league_id=league_id,
            season=season,
            start_round=start_round,
            end_round=end_round,
            save_individual_rounds=save_individual_rounds
        )

    def scrape_league_table(self, league_id: int, season: str, output_path: str = None, output_file: str = None,
                            save_data: bool = False) -> list[Any]:
        """
        Scrape the league table for a specific league and season.

        :param league_id: League ID (e.g. 4335 for Spanish La Liga)
        :param season: Season (e.g. '2024-2025')
        :param output_path: Optional override for output path from config
        :param output_file: Optional override for output filename from config
        :param save_data: Whether the data is to be saved to disk
        :return: League table data
        """
        return self.scrape_data(
            scraper_func=self.api_client.get_league_table,
            save_data=save_data,
            # output_path=output_path,
            # output_file=output_file,
            data_type="league_table",
            league_id=league_id,
            season=season
        )

    def scrape_countries_to_db(self, save_to_file: bool = False) -> int:
        """
        Scrape countries data and save to database.

        :param save_to_file: Whether to also save to file
        :return: Number of countries saved
        """
        countries = self.api_client.get_all_countries()

        if save_to_file and self.storage:
            self.storage.save(countries, "countries")

        if self.db_storage:
            return self.db_storage.save_countries(countries.get('countries', []))
        return 0

    def scrape_leagues_to_db(self, save_to_file: bool = False) -> int:
        """
        Scrape leagues data and save to database.

        :param save_to_file: Whether to also save to file
        :return: Number of leagues saved
        """
        leagues = self.api_client.get_all_leagues()

        if save_to_file and self.storage:
            self.storage.save(leagues, "all")

        if self.db_storage:
            return self.db_storage.save_leagues(leagues.get('all', []))
        return 0

    def scrape_teams_by_league_to_db(self, league_id: int, save_to_file: bool = False) -> int:
        """
        Scrape teams for a specific league and save to database.

        :param league_id: League ID
        :param save_to_file: Whether to also save to file
        :return: Number of teams saved
        """

        league_name = league_id_to_name(league_id)
        teams = self.api_client.get_teams_in_league(league_name)

        if save_to_file and self.storage:
            self.storage.save(teams, "teams", league_id=league_id)

        if self.db_storage:
            return self.db_storage.save_teams(teams.get('teams', []))
        return 0

    def scrape_matches_to_db(self) -> int:
        """
        Scrape matches for a league and season and save to database.

        :return: Number of matches saved
        """
        # TODO implement this method
        pass

        return 0
