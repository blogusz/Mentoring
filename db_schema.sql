CREATE TABLE countries (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE leagues (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INTEGER REFERENCES countries(id),
    foundation_year INTEGER
);

CREATE TABLE venues (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INTEGER REFERENCES countries(id),
    city VARCHAR(50),
    capacity INTEGER,
    foundation_year INTEGER
);

CREATE TABLE teams (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    short_name VARCHAR(50),
    country_id INTEGER REFERENCES countries(id),
    league_id INTEGER REFERENCES leagues(id),
    venue_id INTEGER REFERENCES venues(id),
    foundation_year INTEGER
);

CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    team_id INTEGER REFERENCES teams(id),
    country_id INTEGER REFERENCES countries(id),
    position VARCHAR(50),
    jersey_number INTEGER,
    birth_date DATE
);

CREATE TABLE matches (
    id INTEGER PRIMARY KEY,
    api_football_id INTEGER,
    home_team_id INTEGER REFERENCES teams(id),
    away_team_id INTEGER REFERENCES teams(id),
    league_id INTEGER REFERENCES leagues(id),
    season VARCHAR(10),
    round INTEGER,
    home_score INTEGER,
    away_score INTEGER,
    match_date DATE,
    match_time TIME,
    venue_id INTEGER REFERENCES venues(id),
    status VARCHAR(50)
);
