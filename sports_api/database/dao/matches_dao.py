from typing import List, Dict, Any
from sports_api.database.db_manager import DatabaseManager


class MatchesDAO:
    """Data Access Object for matches table."""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def save_matches(self, matches: List[Dict[str, Any]]) -> int:
        """Save matches to database."""
        conn = self.db_manager.get_connection()
        count = 0

        with conn.cursor() as cur:
            for match in matches:
                match_id = match.get('idEvent')
                if not match_id:
                    continue

                try:
                    # Check if exists
                    cur.execute("SELECT id FROM matches WHERE id = %s", (match_id,))
                    existing = cur.fetchone()

                    if not existing:
                        league_id = match.get('idLeague')
                        season = match.get('strSeason')
                        home_team_id = match.get('idHomeTeam')
                        away_team_id = match.get('idAwayTeam')
                        event_date = match.get('strTimestamp')
                        home_score = match.get('intHomeScore')
                        away_score = match.get('intAwayScore')
                        round_number = match.get('intRound')
                        status = match.get('strStatus')

                        cur.execute(
                            """
                            INSERT INTO matches (id, league_id, season, home_team_id, away_team_id, event_date, home_score, away_score, round_number, status)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            (match_id, league_id, season, home_team_id, away_team_id, event_date,
                             home_score, away_score, round_number, status)
                        )
                    else:
                        # Ignore existing match
                        print(f'Match {match_id} already exists.')
                    count += 1
                except Exception as e:
                    print(f"Error saving match {match_id}: {e}")

            conn.commit()
        return count
