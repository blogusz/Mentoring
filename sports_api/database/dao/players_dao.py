from typing import List, Dict, Any
from sports_api.database.db_manager import DatabaseManager


class PlayersDAO:
    """Data Access Object for players table."""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def save_players(self, players: List[Dict[str, Any]]) -> int:
        """Save players to database."""
        conn = self.db_manager.get_connection()
        count = 0

        with conn.cursor() as cur:
            for player in players:
                player_id = player.get('idPlayer')
                if not player_id:
                    continue

                try:
                    # Check if exists
                    cur.execute("SELECT id FROM players WHERE id = %s", (player_id,))
                    existing = cur.fetchone()

                    if not existing:
                        player_name = player.get('strPlayer')
                        team_id = player.get('idTeam')
                        nationality = player.get('strNationality')
                        date_born = player.get('dateBorn')
                        position = player.get('strPosition')
                        height = player.get('strHeight')
                        weight = player.get('strWeight')
                        jersey_number = player.get('strNumber')

                        cur.execute(
                            """
                            INSERT INTO players (id, name, team_id, nationality, date_born, position, height, weight, jersey_number)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            (player_id, player_name, team_id, nationality, date_born, position, height, weight,
                             jersey_number)
                        )
                    else:
                        print(f'Player {player.get("strPlayer")} already exists with id {player_id}.')

                    count += 1
                except Exception as e:
                    print(f"Error saving player {player.get('strPlayer')}: {e}")

            conn.commit()
        return count
