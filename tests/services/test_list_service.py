import pytest
from unittest.mock import Mock, patch

from sports_api.config import Config
from sports_api.services.list_service import ListService


@pytest.fixture
def mock_config():
    config = Mock(spec=Config)
    config.get_credentials.return_value = ('test_api_key', 'http://test.com/api')
    return config


@pytest.fixture
def list_service(mock_config):
    return ListService(mock_config)


class TestListService:
    @patch.object(ListService, '_make_request')
    def test_get_all_leagues(self, mock_request, list_service):
        mock_request.return_value = {
            'leagues': [
                {'id': '4335', 'name': 'Spanish La Liga'},
                {'id': '4336', 'name': 'English Premier League'}
            ]
        }

        result = list_service.get_all_leagues()

        mock_request.assert_called_once_with('all_leagues.php')
        assert result == {
            'leagues': [
                {'id': '4335', 'name': 'Spanish La Liga'},
                {'id': '4336', 'name': 'English Premier League'}
            ]
        }

    @patch.object(ListService, '_make_request')
    def test_get_all_countries(self, mock_request, list_service):
        mock_request.return_value = {
            'countries': [
                {'name': 'Spain'},
                {'name': 'England'}
            ]
        }

        result = list_service.get_all_countries()

        mock_request.assert_called_once_with('all_countries.php')
        assert result == {
            'countries': [
                {'name': 'Spain'},
                {'name': 'England'}
            ]
        }

    @patch.object(ListService, '_make_request')
    def test_get_all_leagues_in_country(self, mock_request, list_service):
        mock_request.return_value = {
            'leagues': [
                {'name': 'La Liga'},
                {'name': 'Copa del Rey'}
            ]
        }

        result = list_service.get_all_leagues_in_country('Spain', 'Soccer')

        mock_request.assert_called_once_with('search_all_leagues.php?c=Spain&s=Soccer')
        assert result == {
            'leagues': [
                {'name': 'La Liga'},
                {'name': 'Copa del Rey'}
            ]
        }

    @patch.object(ListService, '_make_request')
    def test_get_all_seasons_in_league(self, mock_request, list_service):
        mock_request.return_value = {
            'seasons': [
                {'strSeason': '2023-2024'},
                {'strSeason': '2022-2023'},
                {'strSeason': '2021-2022'}
            ]
        }

        result = list_service.get_all_seasons_in_league(4335)

        mock_request.assert_called_once_with('search_all_seasons.php?id=4335')
        assert result == {
            'seasons': [
                {'strSeason': '2023-2024'},
                {'strSeason': '2022-2023'},
                {'strSeason': '2021-2022'}
            ]
        }

    @patch.object(ListService, '_make_request')
    def test_get_all_teams_in_league(self, mock_request, list_service):
        mock_request.return_value = {
            'teams': [
                {'name': 'Barcelona'},
                {'name': 'Real Madrid'}
            ]
        }

        result = list_service.get_all_teams_in_league('Spanish La Liga')

        mock_request.assert_called_once_with('search_all_teams.php?l=Spanish La Liga')
        assert result == {
            'teams': [
                {'name': 'Barcelona'},
                {'name': 'Real Madrid'}
            ]
        }

    @patch.object(ListService, '_make_request')
    def test_get_all_users_loved_teams_and_players(self, mock_request, list_service):
        mock_request.return_value = {
            'players': [{'name': 'Messi'}],
            'teams': [{'name': 'Barcelona'}]
        }

        result = list_service.get_all_users_loved_teams_and_players('testuser')

        mock_request.assert_called_once_with('searchloves.php?u=testuser')
        assert result == {
            'players': [{'name': 'Messi'}],
            'teams': [{'name': 'Barcelona'}]
        }

    @patch.object(ListService, '_make_request')
    def test_get_all_sports(self, mock_request, list_service):
        mock_request.return_value = {
            'sports': [
                {'name': 'Soccer'},
                {'name': 'Basketball'}
            ]
        }

        result = list_service.get_all_sports()

        mock_request.assert_called_once_with('all_sports.php')
        assert result == {
            'sports': [
                {'name': 'Soccer'},
                {'name': 'Basketball'}
            ]
        }

    @patch.object(ListService, '_make_request')
    def test_get_all_teams_details_in_league(self, mock_request, list_service):
        mock_request.return_value = {
            'teams': [
                {'idTeam': '133604', 'strTeam': 'Barcelona', 'strLeague': 'La Liga'},
                {'idTeam': '133602', 'strTeam': 'Real Madrid', 'strLeague': 'La Liga'}
            ]
        }

        result = list_service.get_all_teams_details_in_league(4335)

        mock_request.assert_called_once_with('lookup_all_teams.php?id=4335')
        assert result == {
            'teams': [
                {'idTeam': '133604', 'strTeam': 'Barcelona', 'strLeague': 'La Liga'},
                {'idTeam': '133602', 'strTeam': 'Real Madrid', 'strLeague': 'La Liga'}
            ]
        }

    @patch.object(ListService, '_make_request')
    def test_get_all_players_in_team(self, mock_request, list_service):
        mock_request.return_value = {
            'players': [
                {'idPlayer': '34145937', 'strPlayer': 'Lionel Messi'},
                {'idPlayer': '34145938', 'strPlayer': 'Luis Suarez'}
            ]
        }

        result = list_service.get_all_players_in_team(133604)

        mock_request.assert_called_once_with('lookup_all_players.php?id=133604')
        assert result == {
            'players': [
                {'idPlayer': '34145937', 'strPlayer': 'Lionel Messi'},
                {'idPlayer': '34145938', 'strPlayer': 'Luis Suarez'}
            ]
        }
