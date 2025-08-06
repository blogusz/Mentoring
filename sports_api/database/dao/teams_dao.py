from typing import List, Dict, Any
from sports_api.database.db_manager import DatabaseManager


class TeamsDAO:
    """Data Access Object for teams table."""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def save_teams(self, teams: List[Dict[str, Any]]) -> int:
        """Save teams to database."""
        conn = self.db_manager.get_connection()
        count = 0

        with conn.cursor() as cur:
            for team in teams:
                team_id = team.get('idTeam')
                if not team_id:
                    continue

                try:
                    # Check if exists
                    cur.execute("SELECT id FROM teams WHERE id = %s", (team_id,))
                    existing = cur.fetchone()

                    if not existing:
                        team_name = team.get('strTeam')
                        alternate_names = team.get('strTeamAlternate')
                        short_name = team.get('strTeamShort')
                        foundation_year = team.get('intFormedYear')
                        sport = team.get('strSport')
                        league_id = team.get('idLeague')
                        venue_id = team.get('idVenue')
                        location = team.get('strLocation')
                        country_name = team.get('strCountry')

                        cur.execute(
                            """
                            INSERT INTO teams (id, name, alternate_names, short_name, foundation_year, sport, league_id, venue_id, location, country_name)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            (team_id, team_name, alternate_names, short_name, foundation_year, sport, league_id,
                             venue_id, location, country_name)
                        )
                    else:
                        # Ignore existing team
                        print(f'Team {team.get("strTeam")} already exists with id {team_id}.')

                    count += 1
                except Exception as e:
                    print(f"Error saving team {team.get('strTeam')}: {e}")

            conn.commit()
        return count
