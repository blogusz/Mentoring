import pytest
from unittest.mock import Mock, patch

from sports_api.config import Config
from sports_api.services.schedule_service import ScheduleService


@pytest.fixture
def mock_config():
    config = Mock(spec=Config)
    config.get_credentials.return_value = ('test_api_key', 'http://test.com/api')
    return config


@pytest.fixture
def schedule_service(mock_config):
    return ScheduleService(mock_config)


class TestScheduleService:
    @patch.object(ScheduleService, '_make_request')
    def test_get_last_5_events_by_team(self, mock_request, schedule_service):
        mock_request.return_value = {
            'events': [
                {'strEvent': 'Barcelona vs Girona', 'dateEvent': '2024-02-01'},
                {'strEvent': 'Barcelona vs Sevilla', 'dateEvent': '2024-02-08'}
            ]
        }

        result = schedule_service.get_last_5_events_by_team(133602)

        mock_request.assert_called_once_with('eventslast.php?id=133602')
        assert result == {
            'events': [
                {'strEvent': 'Barcelona vs Girona', 'dateEvent': '2024-02-01'},
                {'strEvent': 'Barcelona vs Sevilla', 'dateEvent': '2024-02-08'}
            ]
        }

    @patch.object(ScheduleService, '_make_request')
    def test_get_events_by_round(self, mock_request, schedule_service):
        mock_request.return_value = {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'intRound': '1'},
                {'strEvent': 'Atletico vs Sevilla', 'intRound': '1'}
            ]
        }

        result = schedule_service.get_events_by_round(4335, 1, '2023-2024')

        mock_request.assert_called_once_with('eventsround.php?id=4335&r=1&s=2023-2024')
        assert result == {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'intRound': '1'},
                {'strEvent': 'Atletico vs Sevilla', 'intRound': '1'}
            ]
        }

    @patch.object(ScheduleService, '_make_request')
    def test_get_events_in_league_by_season(self, mock_request, schedule_service):
        mock_request.return_value = {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'dateEvent': '2024-03-01', 'strSeason': '2023-2024'},
                {'strEvent': 'Atletico vs Sevilla', 'dateEvent': '2024-03-08', 'strSeason': '2023-2024'}
            ]
        }

        result = schedule_service.get_events_in_league_by_season(4335, '2023-2024')

        mock_request.assert_called_once_with('eventsseason.php?id=4335&s=2023-2024')
        assert result == {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'dateEvent': '2024-03-01', 'strSeason': '2023-2024'},
                {'strEvent': 'Atletico vs Sevilla', 'dateEvent': '2024-03-08', 'strSeason': '2023-2024'}
            ]
        }

    @patch.object(ScheduleService, '_make_request')
    def test_get_next_5_events_by_team(self, mock_request, schedule_service):
        mock_request.return_value = {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'dateEvent': '2024-03-01'},
                {'strEvent': 'Barcelona vs Atletico', 'dateEvent': '2024-03-08'}
            ]
        }

        result = schedule_service.get_next_5_events_by_team(133602)  # Barcelona's ID

        mock_request.assert_called_once_with('eventsnext.php?id=133602')
        assert result == {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'dateEvent': '2024-03-01'},
                {'strEvent': 'Barcelona vs Atletico', 'dateEvent': '2024-03-08'}
            ]
        }

    @patch.object(ScheduleService, '_make_request')
    def test_get_next_25_events_by_league(self, mock_request, schedule_service):
        mock_request.return_value = {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'dateEvent': '2024-03-01'},
                {'strEvent': 'Atletico vs Sevilla', 'dateEvent': '2024-03-08'}
            ]
        }

        result = schedule_service.get_next_25_events_by_league(4328)

        mock_request.assert_called_once_with('eventsnextleague.php?id=4328')
        assert result == {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'dateEvent': '2024-03-01'},
                {'strEvent': 'Atletico vs Sevilla', 'dateEvent': '2024-03-08'}
            ]
        }

    @patch.object(ScheduleService, '_make_request')
    def test_get_last_15_events_by_league(self, mock_request, schedule_service):
        mock_request.return_value = {
            'events': [
                {'strEvent': 'Barcelona vs Girona', 'dateEvent': '2024-02-01'},
                {'strEvent': 'Real Madrid vs Sevilla', 'dateEvent': '2024-02-08'}
            ]
        }

        result = schedule_service.get_last_15_events_by_league(4328)

        mock_request.assert_called_once_with('eventspastleague.php?id=4328')
        assert result == {
            'events': [
                {'strEvent': 'Barcelona vs Girona', 'dateEvent': '2024-02-01'},
                {'strEvent': 'Real Madrid vs Sevilla', 'dateEvent': '2024-02-08'}
            ]
        }

    @patch.object(ScheduleService, '_make_request')
    def test_get_events_on_day(self, mock_request, schedule_service):
        mock_request.return_value = {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'dateEvent': '2024-03-01'},
                {'strEvent': 'Atletico vs Sevilla', 'dateEvent': '2024-03-01'}
            ]
        }

        result = schedule_service.get_events_on_day('2024-03-01')

        mock_request.assert_called_once_with('eventsday.php?d=2024-03-01')
        assert result == {
            'events': [
                {'strEvent': 'Barcelona vs Real Madrid', 'dateEvent': '2024-03-01'},
                {'strEvent': 'Atletico vs Sevilla', 'dateEvent': '2024-03-01'}
            ]
        }

    @patch.object(ScheduleService, '_make_request')
    def test_get_tv_events_on_day_with_all_params(self, mock_request, schedule_service):
        mock_request.return_value = {
            'tvevents': [
                {'strEvent': 'Barcelona vs Real Madrid', 'strChannel': 'Peacock_Premium'},
                {'strEvent': 'Arsenal vs Chelsea', 'strChannel': 'Sky Sports'}
            ]
        }

        result = schedule_service.get_tv_events_on_day(
            day='2024-03-01',
            sport='Soccer',
            station_country='United Kingdom',
            channel='Sky Sports'
        )

        mock_request.assert_called_once_with('eventstv.php?d=2024-03-01&s=Soccer&a=United Kingdom&c=Sky Sports')
        assert result == {
            'tvevents': [
                {'strEvent': 'Barcelona vs Real Madrid', 'strChannel': 'Peacock_Premium'},
                {'strEvent': 'Arsenal vs Chelsea', 'strChannel': 'Sky Sports'}
            ]
        }
