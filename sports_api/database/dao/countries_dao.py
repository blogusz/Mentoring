from typing import List, Dict, Any
import uuid
from sports_api.database.db_manager import DatabaseManager


class CountriesDAO:
    """
    Data Access Object for countries table.
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def save_countries(self, countries: List[Dict[str, Any]]) -> int:
        """
        Save countries to database.
        """
        conn = self.db_manager.get_connection()
        count = 0

        with conn.cursor() as cur:
            for country in countries:
                country_name = country.get('name_en')
                if not country_name:
                    continue

                try:
                    # Check if exists
                    cur.execute("SELECT id FROM countries WHERE name = %s", (country_name,))
                    existing = cur.fetchone()

                    if not existing:
                        country_id = str(uuid.uuid4())
                        cur.execute(
                            "INSERT INTO countries (id, name) VALUES (%s, %s)",
                            (country_id, country_name)
                        )
                    else:
                        # Ignore existing country
                        country_id = existing['id']
                        print(f'Country {country_name} already exists with id {country_id}.')

                    count += 1
                except Exception as e:
                    print(f"Error saving country {country_name}: {e}")

            conn.commit()
        return count
