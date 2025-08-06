import psycopg
from psycopg.rows import dict_row
from sports_api.config import Config


class DatabaseManager:
    """
    Handles database connections and basic operations.
    """

    def __init__(self, config: Config):
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
