CREATE TABLE countries (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE leagues (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    alternate_name VARCHAR(100),
    sport VARCHAR(50)
);

CREATE TABLE venues (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    alternate_names VARCHAR(100),
    sport VARCHAR(50),
    capacity INTEGER,
    country_name VARCHAR(100),
    location VARCHAR(100),
    foundation_year INTEGER
);

CREATE TABLE teams (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    alternate_names VARCHAR(100),
    short_name VARCHAR(50),
    foundation_year INTEGER,
    sport VARCHAR(50),
    league_id INTEGER REFERENCES leagues(id),
    venue_id INTEGER REFERENCES venues(id),
    location VARCHAR(100),
    country_name VARCHAR(100)
);

CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    team_id INTEGER REFERENCES teams(id),
    national_country_id INTEGER REFERENCES countries(id),
    position VARCHAR(50),
    height VARCHAR(20),
    weight VARCHAR(20),
    jersey_number INTEGER,
    birth_date DATE
);

CREATE TABLE matches (
    id INTEGER PRIMARY KEY,
    league_id INTEGER REFERENCES leagues(id),
    season VARCHAR(10),
    home_team_id INTEGER REFERENCES teams(id),
    away_team_id INTEGER REFERENCES teams(id),
    event_date DATE,
    home_score INTEGER,
    away_score INTEGER,
    round_number INTEGER,
    status VARCHAR(50)
);
