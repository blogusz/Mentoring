from typing import List, Dict, Any
from sports_api.database.db_manager import DatabaseManager


class LeaguesDAO:
    """
    Data Access Object for leagues table.
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def save_leagues(self, leagues: List[Dict[str, Any]]) -> int:
        """
        Save leagues to database.
        """
        conn = self.db_manager.get_connection()
        count = 0

        with conn.cursor() as cur:
            for league in leagues:
                league_name = league.get('strLeague')
                if not league_name:
                    continue

                try:
                    # Check if exists
                    cur.execute("SELECT id FROM leagues WHERE name = %s", (league_name,))
                    existing = cur.fetchone()

                    if not existing:
                        league_id = league.get('idLeague')
                        sport = league.get('strSport')
                        alternate_names = league.get('strLeagueAlternate')

                        cur.execute(
                            "INSERT INTO leagues (id, name, sport, alternate_names) VALUES (%s, %s, %s, %s)",
                            (league_id, league_name, sport, alternate_names)
                        )
                    count += 1
                except Exception as e:
                    print(f"Error saving league {league_name}: {e}")

            conn.commit()
        return count
