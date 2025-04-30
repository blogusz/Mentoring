import pytest
from unittest.mock import Mock, patch

from sports_api.config import Config
from sports_api.services.search_service import SearchService


@pytest.fixture
def mock_config():
    config = Mock(spec=Config)
    config.get_credentials.return_value = ('test_api_key', 'http://test.com/api')
    return config


@pytest.fixture
def search_service(mock_config):
    return SearchService(mock_config)


class TestSearchService:
    @patch.object(SearchService, '_make_request')
    def test_search_team_by_name(self, mock_request, search_service):
        mock_request.return_value = {'teams': [{'name': 'Barcelona'}]}

        result = search_service.search_team_by_name('Barcelona')

        mock_request.assert_called_once_with('searchteams.php?t=Barcelona')
        assert result == {'teams': [{'name': 'Barcelona'}]}

    @patch.object(SearchService, '_make_request')
    def test_search_team_by_shortcode(self, mock_request, search_service):
        mock_request.return_value = {'teams': [{'shortcode': 'FCB'}]}

        result = search_service.search_team_by_shortcode('FCB')

        mock_request.assert_called_once_with('searchteams.php?t=FCB')
        assert result == {'teams': [{'shortcode': 'FCB'}]}

    @patch.object(SearchService, '_make_request')
    def test_search_player_by_name(self, mock_request, search_service):
        mock_request.return_value = {'players': [{'name': 'Messi'}]}

        result = search_service.search_player_by_name('Messi')

        mock_request.assert_called_once_with('searchplayers.php?p=Messi')
        assert result == {'players': [{'name': 'Messi'}]}

    @patch.object(SearchService, '_make_request')
    def test_search_event_by_name(self, mock_request, search_service):
        mock_request.return_value = {'events': [{'name': 'Barcelona_vs_Real_Madrid'}]}

        result = search_service.search_event_by_name('Barcelona_vs_Real_Madrid')

        mock_request.assert_called_once_with('searchevents.php?e=Barcelona_vs_Real_Madrid')
        assert result == {'events': [{'name': 'Barcelona_vs_Real_Madrid'}]}

    @patch.object(SearchService, '_make_request')
    def test_search_event_by_file_name(self, mock_request, search_service):
        mock_request.return_value = {'events': [{'filename': 'Spanish_La_Liga_2023-10-28_Barcelona_vs_Real_Madrid'}]}

        result = search_service.search_event_by_file_name('Spanish_La_Liga_2023-10-28_Barcelona_vs_Real_Madrid')

        mock_request.assert_called_once_with('searchfilename.php?e=Spanish_La_Liga_2023-10-28_Barcelona_vs_Real_Madrid')
        assert result == {'events': [{'filename': 'Spanish_La_Liga_2023-10-28_Barcelona_vs_Real_Madrid'}]}

    @patch.object(SearchService, '_make_request')
    def test_search_venue_by_name(self, mock_request, search_service):
        mock_request.return_value = {'venues': [{'name': 'Camp Nou'}]}

        result = search_service.search_venue_by_name('Camp Nou')

        mock_request.assert_called_once_with('searchvenues.php?t=Camp Nou')
        assert result == {'venues': [{'name': 'Camp Nou'}]}

    @patch.object(SearchService, '_make_request')
    def test_search_all_players_from_team(self, mock_request, search_service):
        mock_request.return_value = {'players': [{'team': 'Barcelona'}]}

        result = search_service.search_all_players_from_team('Barcelona')

        mock_request.assert_called_once_with('searchplayers.php?t=Barcelona')
        assert result == {'players': [{'team': 'Barcelona'}]}
