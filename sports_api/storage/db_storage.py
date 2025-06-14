from typing import Any, Dict, List
import psycopg
from psycopg.rows import dict_row
import uuid

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
            return f"Saved {self.save_leagues(data.get('all', []))} leagues"
        elif data_type == "teams":
            return f"Saved {self.save_teams(data.get('teams', []))} teams"
        elif data_type == "rounds" or data_type == "matches":
            # Handle both single round data and multiple matches
            matches = data.get('events', []) if isinstance(data, dict) else data
            return f"Saved {self.save_matches(matches)} matches"
        elif data_type == "venues":
            return f"Saved {self.save_venues(data.get('venues', []))} venues"
        elif data_type == "players":
            return f"Saved {self.save_players(data.get('player', []))} players"
        else:
            return f"Unknown data type: {data_type}"

    def save_countries(self, countries: List[Dict[str, Any]]) -> int:
        """
        Save countries to database using UUID as primary key.
        
        This function checks if a country already exists (by name) before inserting,
        and generates a UUID for new countries.
        """
        conn = self.get_connection()
        count = 0

        with conn.cursor() as cur:
            for country in countries:
                country_name = country.get('name_en')
                if not country_name:
                    continue
                try:
                    # Check if country already exists
                    cur.execute(
                        """
                        SELECT id FROM countries
                        WHERE name = %s
                        """,
                        country_name
                    )
                    existing = cur.fetchone()

                    if not existing:
                        # Generate UUID for new country
                        country_id = str(uuid.uuid4())
                        cur.execute(
                            """
                            INSERT INTO countries (id, name)
                            VALUES (%s, %s)
                            """,
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

    def save_leagues(self, leagues: List[Dict[str, Any]]) -> int:
        """
        Save leagues to database.
        """
        conn = self.get_connection()
        count = 0

        with conn.cursor() as cur:
            for league in leagues:
                league_name = league.get('strLeague')
                if not league_name:
                    continue
                try:
                    # Check if league already exists
                    cur.execute(
                        """
                        SELECT id FROM leagues
                        WHERE name = %s
                        """,
                        league_name
                    )
                    existing = cur.fetchone()

                    if not existing:
                        league_id = league.get('idLeague')
                        sport = league.get('strSport')
                        alternate_names = league.get('strLeagueAlternate')

                        cur.execute(
                            """
                            INSERT INTO leagues (id, name, sport, alternate_names)
                            VALUES (%s, %s, %s, %s)
                            """,
                            (league_id, league_name, sport, alternate_names)
                        )
                    else:
                        # Ignore existing league
                        league_id = existing['id']
                        print(f'League {league_name} already exists with id {league_id}.')

                    count += 1
                except Exception as e:
                    print(f"Error saving league {league_name}: {e}")

            conn.commit()

        return count

    def save_teams(self, teams: List[Dict[str, Any]]) -> int:
        """
        Save teams to database.
        """

        conn = self.get_connection()
        count = 0
        with conn.cursor() as cur:
            for team in teams:
                team_id = team.get('idTeam')
                if not team_id:
                    continue
                try:
                    # Check if team already exists
                    cur.execute(
                        """
                        SELECT id FROM teams
                        WHERE id = %s
                        """,
                        team_id
                    )
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
                        print(f'Team {team_name} already exists with id {team_id}.')

                    count += 1
                except Exception as e:
                    print(f"Error saving team {team_name}: {e}")

            conn.commit()

        return count

    def save_matches(self, matches: List[Dict[str, Any]]) -> int:
        """
        Save matches to database.
        """
        conn = self.get_connection()
        count = 0
        with conn.cursor() as cur:
            for match in matches:
                match_id = match.get('idEvent')
                if not match_id:
                    continue
                try:
                    # Check if match already exists
                    cur.execute(
                        """
                        SELECT id FROM matches
                        WHERE id = %s
                        """,
                        match_id
                    )
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
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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

    def save_venues(self, venues: List[Dict[str, Any]]) -> int:
        """
        Save venues to database.
        """
        conn = self.get_connection()
        count = 0
        with conn.cursor() as cur:
            for venue in venues:
                venue_id = venue.get('idVenue')
                if not venue_id:
                    continue
                try:
                    # Check if venue already exists
                    cur.execute(
                        """
                        SELECT id FROM venues
                        WHERE id = %s
                        """,
                        venue_id
                    )
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
                        print(f'Venue {venue_name} already exists with id {venue_id}.')

                    count += 1
                except Exception as e:
                    print(f"Error saving venue {venue_name}: {e}")

            conn.commit()

        return count

    def save_players(self, players: List[Dict[str, Any]]) -> int:
        """
        Save players to database.
        """
        # this method should use data received from the lookup_all_players.php endpoint

        # Exemplary data. This should be retreived!: {"player":[{"idPlayer":"34163698",
        # "idTeam":"133604",
        # "strNationality":"England",
        # "strPlayer":"Ben White",
        # "strTeam":"Arsenal",
        # "dateBorn":"1997-11-08",
        # "dateDied":null,
        # "strNumber":"4",
        # "strSigning":"£25.20m",
        # "strWage":"£6,240,000 (£120,000 a week)",
        # "strBirthLocation":"Poole, England",
        # "strEthnicity":"White",
        # "strStatus":"Active""
        # strGender":"Male",
        # "strSide":"Right",
        # "strPosition":"Right-Back",
        # "strHeight":"6 ft 1 in (1.85 m)",
        # "strWeight":"78 kg"}
        # ]}

        conn = self.get_connection()
        count = 0
        with conn.cursor() as cur:
            for player in players:
                player_id = player.get('idPlayer')
                if not player_id:
                    continue
                try:
                    # Check if player already exists
                    cur.execute(
                        """
                        SELECT id FROM players
                        WHERE id = %s
                        """,
                        player_id
                    )
                    existing = cur.fetchone()

                    if not existing:

                    else:
                        # Ignore existing player
                        print(f'Player {player_name} already exists with id {player_id}.')

                    count += 1
                except Exception as e:
                    print(f"Error saving player {player_name}: {e}")

            conn.commit()

        return count
