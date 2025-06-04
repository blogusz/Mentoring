from typing import Any, Dict, List
import psycopg
from psycopg.rows import dict_row

from sports_api.config import Config
from sports_api.storage.storage_interface import StorageInterface


class DatabaseStorage(StorageInterface):
    """
    Database storage implementation for sports data.
    """

    def __init__(self, config: Config):
        """
        Initialize database storage with configuration.
        """
        self.config = config
        self._connection = None

    def get_connection(self):
        """
        Get or create database connection.
        """
        if not self._connection or self._connection.closed:
            db_config = self.config.get_database_config()
            self._connection = psycopg.connect(
                host=db_config['host'],
                port=db_config['port'],
                dbname=db_config['dbname'],
                user=db_config['user'],
                password=db_config['password'],
                row_factory=dict_row
            )
        return self._connection

    def close(self):
        """
        Close the database connection.
        """
        if self._connection and not self._connection.closed:
            self._connection.close()
            self._connection = None

    def save(self, data: Any, data_type: str = None, **kwargs) -> str:
        """
        Save data using the appropriate method based on data_type.
        
        :param data: Data to be saved
        :param data_type: Type of data (countries, leagues, teams, matches, etc.)
        :param kwargs: Additional parameters
        :return: Identifier or count of saved items
        """
        if not data:
            return "No data to save"

        if data_type == "countries":
            return f"Saved {self.save_countries(data.get('countries', []))} countries"
        elif data_type == "leagues":
            return f"Saved {self.save_leagues(data.get('leagues', []))} leagues"
        elif data_type == "teams":
            return f"Saved {self.save_teams(data.get('teams', []))} teams"
        elif data_type == "rounds" or data_type == "matches":
            # Handle both single round data and multiple matches
            matches = data.get('events', []) if isinstance(data, dict) else data
            return f"Saved {self.save_matches(matches)} matches"
        else:
            return f"Unknown data type: {data_type}"

    # TODO implement all class methods
    def save_countries(self, countries: List[Dict[str, Any]]) -> int:
        """
        Save countries to database.
        """
        pass

        return 0

    def save_leagues(self, leagues: List[Dict[str, Any]]) -> int:
        """
        Save leagues to database.
        """
        pass

        return 0

    def save_teams(self, teams: List[Dict[str, Any]]) -> int:
        """
        Save teams to database.
        """
        pass

        return 0

    def save_matches(self, matches: List[Dict[str, Any]]) -> int:
        """
        Save matches to database.
        """
        pass

        return 0
