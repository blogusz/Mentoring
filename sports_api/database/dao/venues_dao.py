from typing import List, Dict, Any
from sports_api.database.db_manager import DatabaseManager


class VenuesDAO:
    """Data Access Object for venues table."""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def save_venues(self, venues: List[Dict[str, Any]]) -> int:
        """Save venues to database."""
        conn = self.db_manager.get_connection()
        count = 0

        with conn.cursor() as cur:
            for venue in venues:
                venue_id = venue.get('idVenue')
                if not venue_id:
                    continue

                try:
                    # Check if exists
                    cur.execute("SELECT id FROM venues WHERE id = %s", (venue_id,))
                    existing = cur.fetchone()

                    if not existing:
                        venue_name = venue.get('strVenue')
                        alternate_names = venue.get('strVenueAlternate')
                        sport = venue.get('strSport')
                        capacity = venue.get('intCapacity')
                        country_name = venue.get('strCountry')
                        location = venue.get('strLocation')
                        foundation_year = venue.get('intFormedYear')

                        cur.execute(
                            """
                            INSERT INTO venues (id, name, alternate_names, sport, capacity, country_name, location, foundation_year)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            (venue_id, venue_name, alternate_names, sport, capacity, country_name, location,
                             foundation_year)
                        )
                    else:
                        # Ignore existing venue
                        print(f'Venue {venue.get("strVenue")} already exists with id {venue_id}.')

                    count += 1
                except Exception as e:
                    print(f"Error saving venue {venue.get('strVenue')}: {e}")

            conn.commit()
        return count
