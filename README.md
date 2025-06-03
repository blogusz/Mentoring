# Sports API

This package provides a simple interface for interacting with the Sports DB API (https://www.thesportsdb.com/api.php).
It abstracts away the low-level API details and provides a clean, easy-to-use interface for retrieving sports data.

## Usage

The `ApiClient` class is the main entry point for interacting with the API. It provides methods for retrieving data from
the API without having to worry about the underlying implementation details.

### Creating an API Client

```python
from sports_api import ApiClient

# Create an API client with default configuration (loaded from config file)
api_client = ApiClient()

# Or create an API client with custom API key and base URL
api_client = ApiClient(api_key="your_api_key", base_url="https://www.thesportsdb.com/api/v1/json")
```

### Configuration

The API client can be configured in several ways:

1. **YAML Configuration**: Create a `config/config.yaml` file with the following structure:

```yaml
api:
  key: your_api_key
  base_url: https://www.thesportsdb.com/api/v1/json
data:
  output_path: retrieved_data/
  default_file: data.json
```

2. **Direct Configuration**: Pass the API key and base URL directly to the ApiClient constructor:

```python
api_client = ApiClient(api_key="your_api_key", base_url="https://www.thesportsdb.com/api/v1/json")
```

3. **Config Object**: Create a Config object and pass it to the ApiClient:

```python
from sports_api.config import Config

config = Config(api_key="your_api_key", base_url="https://www.thesportsdb.com/api/v1/json")
api_client = ApiClient(config=config)
```

### Retrieving Data

The API client provides methods for retrieving different types of data:

#### Rounds Data

```python
# Get data for rounds 1-5 of the Spanish La Liga 2024-2025 season
rounds_data = api_client.get_all_rounds(
    league_id=4335,  # Spanish La Liga
    season='2024-2025',
    start_round=1,
    end_round=5,
    save_data=True,  # Save the data to a file
    output_file='rounds_data.json'  # Optional file name
)
```

#### Search Data

```python
# Search for a team by name
team_data = api_client.search_team("Barcelona")

# Search for a team by shortcode
team_data = api_client.search_team_by_shortcode("FCB")

# Search for a player
player_data = api_client.search_player("Messi")

# Search for an event by name
event_data = api_client.search_event("Barcelona_vs_Real_Madrid")

# Search for an event by file name
event_data = api_client.search_event_by_file_name("Spanish_La_Liga_2023-10-28_Barcelona_vs_Real_Madrid")

# Search for a venue
venue_data = api_client.search_venue("Camp Nou")
```

#### List Data

```python
# Get a list of all leagues
leagues = api_client.get_all_leagues()

# Get a list of all countries
countries = api_client.get_all_countries()

# Get a list of all leagues in a country
leagues_in_spain = api_client.get_leagues_in_country("Spain")

# Get a list of all teams in a league
teams_in_la_liga = api_client.get_teams_in_league("Spanish La Liga")

# Get a list of all seasons in a league
seasons = api_client.get_seasons_in_league(4335)  # Spanish La Liga

# Get a list of users loved teams and players
loved_items = api_client.get_users_loved_teams_and_players("username")
```

#### Lookup Data

```python
# Get player details
player = api_client.get_player_details(34145937)

# Get venue details
venue = api_client.get_venue_details(16163)

# Get player honours
honours = api_client.get_player_honours(34147178)

# Get player milestones
milestones = api_client.get_player_milestones(34161397)

# Get player former teams
former_teams = api_client.get_player_former_teams(34147178)

# Get player contracts
contracts = api_client.get_player_contracts(34147178)

# Get event player results
player_results = api_client.get_event_player_results(652890)

# Get league table
table = api_client.get_league_table(4335, "2023-2024")

# Get team equipment (kits)
equipment = api_client.get_team_equipment(133597)
```

#### Schedule Data

```python
# Get last 5 events for a team
last_events = api_client.get_last_5_events_by_team(133602)

# Get events for a specific round in a league
round_events = api_client.get_events_by_round(4335, 1, "2023-2024")

# Get all events in a league for a season
season_events = api_client.get_events_in_league_by_season(4335, "2023-2024")
```

## Data Scraping

The package also includes a `DataScraper` class for scheduled data collection:

```python
from sports_api.config import Config
from sports_api.data_scraper import DataScraper

config = Config()
scraper = DataScraper(config)

# Scrape league table data
table_data = scraper.scrape_league_table(
    league_id=4335,  # Spanish La Liga
    season='2024-2025',
    save_data=True
)

# Scrape all rounds for a league
rounds_data = scraper.scrape_all_rounds(
    league_id=4335,
    season='2024-2025',
    start_round=1,
    end_round=5,
    save_all_rounds=True
)
```

## Scheduler

The package includes a scheduler module that allows you to set up automated data collection tasks. The scheduler uses
the `schedule` library to run tasks at specified intervals.

```python
import schedule
from sports_api.config import Config
from sports_api.data_scraper import DataScraper


def job_scrape_league_table():
    print("Scraping league table...")
    config = Config()
    scraper = DataScraper(config)
    scraper.scrape_league_table(
        league_id=4335,  # Spanish La Liga
        season='2024-2025',
        save_data=True,
    )


def job_scrape_all_rounds():
    print("Scraping all rounds...")
    config = Config()
    scraper = DataScraper(config)
    scraper.scrape_all_rounds(
        league_id=4335,  # Spanish La Liga
        season='2024-2025',
        start_round=1,
        save_all_rounds=True,
        save_individual_rounds=True,
    )


def main():
    # Schedule jobs to run every Sunday at 23:30
    schedule.every().sunday.at("23:30").do(job_scrape_league_table)
    schedule.every().sunday.at("23:30").do(job_scrape_all_rounds)

    # Run the scheduler
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
```

This allows you to automatically collect data at regular intervals without manual intervention. You can customize the
schedule to run daily, weekly, or at specific times as needed.

## Implementation Details

The API client is implemented using a service-oriented architecture:

- `ApiClient`: The main entry point for interacting with the API. It delegates calls to the appropriate service.
- `Config`: Handles API configuration, including loading API keys from YAML configuration files.
- `DataScraper`: Provides utilities for scraping and saving data from the API.
- `services`: Contains the service implementations that handle API requests:
    - `BaseService`: Base class that provides common functionality for all services, including the `_make_request`
      method.
    - `RoundsService`: Handles retrieving data for rounds.
    - `SearchService`: Handles searching for teams, players, and events.
    - `ListService`: Handles retrieving lists of leagues, countries, teams, etc.
    - `LookupService`: Handles looking up details for players, teams, events, etc.
    - `ScheduleService`: Handles retrieving schedule data.

Each service class directly constructs and calls the appropriate API endpoints. Methods marked with the
`@premium_required` decorator require a premium API subscription.