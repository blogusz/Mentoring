from typing import Any

from sports_api.config import Config
from sports_api.storage.storage_interface import StorageInterface
from sports_api.database.db_manager import DatabaseManager
from sports_api.database.dao.countries_dao import CountriesDAO
from sports_api.database.dao.leagues_dao import LeaguesDAO
from sports_api.database.dao.teams_dao import TeamsDAO
from sports_api.database.dao.matches_dao import MatchesDAO
from sports_api.database.dao.venues_dao import VenuesDAO
from sports_api.database.dao.players_dao import PlayersDAO


class DatabaseStorage(StorageInterface):
    """
    Database storage implementation for sports data.
    Simple interface that delegates to appropriate DAOs.
    """

    def __init__(self, config: Config):
        self.config = config
        self.db_manager = DatabaseManager(config)

        # Initialize DAOs
        self.countries_dao = CountriesDAO(self.db_manager)
        self.leagues_dao = LeaguesDAO(self.db_manager)
        self.matches_dao = MatchesDAO(self.db_manager)
        self.players_dao = PlayersDAO(self.db_manager)
        self.teams_dao = TeamsDAO(self.db_manager)
        self.venues_dao = VenuesDAO(self.db_manager)

    def close(self):
        """
        Close the database connection.
        """
        self.db_manager.close()

    def save(self, data: Any, data_type: str = None, **kwargs) -> str:
        """
        Save data using the appropriate DAO based on data_type.
        """
        if not data:
            return "No data to save"

        if data_type == "countries":
            count = self.countries_dao.save_countries(data.get('countries', []))
            return f"Saved {count} countries"
        elif data_type == "leagues":
            count = self.leagues_dao.save_leagues(data.get('all', []))
            return f"Saved {count} leagues"
        elif data_type == "teams":
            count = self.teams_dao.save_teams(data.get('teams', []))
            return f"Saved {count} teams"
        elif data_type == "rounds" or data_type == "matches" or data_type == "season_matches":
            # Handle both single round data and multiple matches
            matches = data.get('events', []) if isinstance(data, dict) else data
            count = self.matches_dao.save_matches(matches)
            return f"Saved {count} matches"
        elif data_type == "venues":
            count = self.venues_dao.save_venues(data.get('venues', []))
            return f"Saved {count} venues"
        elif data_type == "players":
            count = self.players_dao.save_players(data.get('player', []))
            return f"Saved {count} players"
        else:
            return f"Unknown data type: {data_type}"
