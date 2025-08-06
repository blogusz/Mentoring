import os

from sports_api.config import Config


def league_id_to_name(league_id: int) -> str:
    """
    Map league IDs to their names for file naming purposes.
    """
    league_mapping = {
        4328: "premier_league",
        4331: "bundesliga",
        4332: "serie_a",
        4334: "ligue_1",
        4335: "laliga",
        # Add more leagues as needed
    }
    return league_mapping.get(league_id, f"league_{league_id}")


def generate_file_path(config: Config, data_type: str, league_id: int = None, season: str = None, round_num: int = None,
                       **kwargs) -> tuple[str, str]:
    """
    Generate appropriate file path and name based on the data type and parameters.

    :param config: Config object
    :param data_type: Type of data (e.g., 'rounds', 'league_table')
    :param league_id: Optional league ID
    :param season: Optional season string (e.g., '2024-2025')
    :param round_num: Optional round number
    :param kwargs: Additional parameters for specialized naming
    :return: Tuple of (directory_path, filename)
    """
    if not config:
        raise ValueError("Config object is required to generate file path.")

    base_path = config.get_output_settings()['output_path']

    # Get league name from ID or use the ID as string
    league_name = league_id_to_name(league_id) if league_id else ""

    # Format season for filenames (2024-2025 -> 2024_2025)
    formatted_season = season.replace("-", "_") if season else ""

    if data_type == "rounds":
        directory = os.path.join(base_path, "rounds", league_name, formatted_season)

        if round_num is None:
            # Multiple rounds
            start_round = kwargs.get('start_round', 1)
            end_round = kwargs.get('end_round', 38)
            filename = f"{league_name}_{formatted_season}_rounds_{start_round}_to_{end_round}.json"
        else:
            # Single round
            filename = f"{league_name}_{formatted_season}_round_{round_num}.json"

    elif data_type == "league_table":
        # For league table data
        directory = os.path.join(base_path, "tables", league_name, formatted_season)
        filename = f"{league_name}_{formatted_season}_table.json"

    elif data_type == "season_matches":
        directory = os.path.join(base_path, "matches", league_name, formatted_season)
        filename = f"{league_name}_{formatted_season}_all_matches.json"

    else:
        # Default case (works for countries, leagues, teams, players, venues, etc.)
        directory = os.path.join(base_path, data_type)
        filename = f"{data_type}_{league_name}_{formatted_season}.json"

    return directory, filename
