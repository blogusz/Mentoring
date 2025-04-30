import pytest
from unittest.mock import Mock, patch

from sports_api.config import Config
from sports_api.services.lookup_service import LookupService


@pytest.fixture
def mock_config():
    config = Mock(spec=Config)
    config.get_credentials.return_value = ('test_api_key', 'http://test.com/api')
    return config


@pytest.fixture
def lookup_service(mock_config):
    return LookupService(mock_config)


class TestLookupService:
    @patch.object(LookupService, '_make_request')
    def test_get_player_details(self, mock_request, lookup_service):
        mock_request.return_value = {
            'players': [{
                'idPlayer': '34145937',
                'strPlayer': 'Lionel Messi',
                'strTeam': 'Inter Miami'
            }]
        }

        result = lookup_service.get_player_details(34145937)

        mock_request.assert_called_once_with('lookupplayer.php?id=34145937')
        assert result == {
            'players': [{
                'idPlayer': '34145937',
                'strPlayer': 'Lionel Messi',
                'strTeam': 'Inter Miami'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_venue_details(self, mock_request, lookup_service):
        mock_request.return_value = {
            'venues': [{
                'idVenue': '16163',
                'strVenue': 'Camp Nou',
                'strCity': 'Barcelona'
            }]
        }

        result = lookup_service.get_venue_details(16163)

        mock_request.assert_called_once_with('lookupvenue.php?id=16163')
        assert result == {
            'venues': [{
                'idVenue': '16163',
                'strVenue': 'Camp Nou',
                'strCity': 'Barcelona'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_player_honours(self, mock_request, lookup_service):
        mock_request.return_value = {
            'honours': [{
                'strHonour': 'FIFA World Cup',
                'strSeason': '2022'
            }]
        }

        result = lookup_service.get_player_honours(34147178)

        mock_request.assert_called_once_with('lookuphonours.php?id=34147178')
        assert result == {
            'honours': [{
                'strHonour': 'FIFA World Cup',
                'strSeason': '2022'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_player_milestones(self, mock_request, lookup_service):
        mock_request.return_value = {
            'milestones': [{
                'idPlayer': '34147178',
                'strMilestone': '100th Goal',
                'strSeason': '2023'
            }]
        }
        result = lookup_service.get_player_milestones(34147178)

        mock_request.assert_called_once_with('lookupmilestones.php?id=34147178')
        assert result == {
            'milestones': [{
                'idPlayer': '34147178',
                'strMilestone': '100th Goal',
                'strSeason': '2023'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_player_former_teams(self, mock_request, lookup_service):
        mock_request.return_value = {
            'formerteams': [{
                'strFormerTeam': 'Barcelona',
                'strJoined': '2004',
                'strDeparted': '2021'
            }]
        }

        result = lookup_service.get_player_former_teams(34147178)

        mock_request.assert_called_once_with('lookupformerteams.php?id=34147178')
        assert result == {
            'formerteams': [{
                'strFormerTeam': 'Barcelona',
                'strJoined': '2004',
                'strDeparted': '2021'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_player_contracts(self, mock_request, lookup_service):
        mock_request.return_value = {
            'contracts': [{
                'idPlayer': '34147178',
                'strTeam': 'Inter Miami',
                'strYearStart': '2023',
                'strYearEnd': '2025'
            }]
        }
        result = lookup_service.get_player_contracts(34147178)

        mock_request.assert_called_once_with('lookupcontracts.php?id=34147178')
        assert result == {
            'contracts': [{
                'idPlayer': '34147178',
                'strTeam': 'Inter Miami',
                'strYearStart': '2023',
                'strYearEnd': '2025'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_event_player_results(self, mock_request, lookup_service):
        mock_request.return_value = {
            'results': [{
                'idEvent': '652890',
                'strPlayer': 'Lionel Messi',
                'strResult': 'Goal 34\''
            }]
        }

        result = lookup_service.get_event_player_results(652890)

        mock_request.assert_called_once_with('eventresults.php?id=652890')
        assert result == {
            'results': [{
                'idEvent': '652890',
                'strPlayer': 'Lionel Messi',
                'strResult': 'Goal 34\''
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_league_table(self, mock_request, lookup_service):
        mock_request.return_value = {
            'table': [{
                'name': 'Barcelona',
                'points': '82',
                'position': '1'
            }]
        }

        result = lookup_service.get_league_table(4335, '2023-2024')

        mock_request.assert_called_once_with('lookuptable.php?l=4335&s=2023-2024')
        assert result == {
            'table': [{
                'name': 'Barcelona',
                'points': '82',
                'position': '1'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_team_equipment(self, mock_request, lookup_service):
        mock_request.return_value = {
            'equipment': [{
                'idTeam': '133597',
                'strEquipment': 'Nike',
                'strSeason': '2023-2024'
            }]
        }

        result = lookup_service.get_team_equipment(133597)

        mock_request.assert_called_once_with('lookupequipment.php?id=133597')
        assert result == {
            'equipment': [{
                'idTeam': '133597',
                'strEquipment': 'Nike',
                'strSeason': '2023-2024'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_league_details(self, mock_request, lookup_service):
        mock_request.return_value = {
            'leagues': [{
                'idLeague': '4346',
                'strLeague': 'La Liga',
                'strCountry': 'Spain'
            }]
        }

        result = lookup_service.get_league_details(4346)

        mock_request.assert_called_once_with('lookupleague.php?id=4346')
        assert result == {
            'leagues': [{
                'idLeague': '4346',
                'strLeague': 'La Liga',
                'strCountry': 'Spain'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_team_details(self, mock_request, lookup_service):
        mock_request.return_value = {
            'teams': [{
                'idTeam': '133604',
                'strTeam': 'Barcelona',
                'strLeague': 'La Liga'
            }]
        }

        result = lookup_service.get_team_details(133604)

        mock_request.assert_called_once_with('lookupteam.php?id=133604')
        assert result == {
            'teams': [{
                'idTeam': '133604',
                'strTeam': 'Barcelona',
                'strLeague': 'La Liga'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_event_details(self, mock_request, lookup_service):
        mock_request.return_value = {
            'events': [{
                'idEvent': '441613',
                'strEvent': 'Barcelona vs Real Madrid',
                'dateEvent': '2024-03-01'
            }]
        }

        result = lookup_service.get_event_details(441613)

        mock_request.assert_called_once_with('lookupevent.php?id=441613')
        assert result == {
            'events': [{
                'idEvent': '441613',
                'strEvent': 'Barcelona vs Real Madrid',
                'dateEvent': '2024-03-01'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_event_statistics(self, mock_request, lookup_service):
        mock_request.return_value = {
            'statistics': [{
                'idEvent': '1032723',
                'strStat': 'Possession',
                'intHome': '60',
                'intAway': '40'
            }]
        }

        result = lookup_service.get_event_statistics(1032723)

        mock_request.assert_called_once_with('lookupeventstats.php?id=1032723')
        assert result == {
            'statistics': [{
                'idEvent': '1032723',
                'strStat': 'Possession',
                'intHome': '60',
                'intAway': '40'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_event_lineup(self, mock_request, lookup_service):
        mock_request.return_value = {
            'lineup': [{
                'idEvent': '1032723',
                'strPlayer': 'Lionel Messi',
                'strPosition': 'Forward'
            }]
        }

        result = lookup_service.get_event_lineup(1032723)

        mock_request.assert_called_once_with('lookuplineup.php?id=1032723')
        assert result == {
            'lineup': [{
                'idEvent': '1032723',
                'strPlayer': 'Lionel Messi',
                'strPosition': 'Forward'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_event_timeline(self, mock_request, lookup_service):
        mock_request.return_value = {
            'timeline': [{
                'idEvent': '1032718',
                'strTimeline': 'Goal',
                'strPlayer': 'Lionel Messi',
                'intTime': '34'
            }]
        }

        result = lookup_service.get_event_timeline(1032718)

        mock_request.assert_called_once_with('lookuptimeline.php?id=1032718')
        assert result == {
            'timeline': [{
                'idEvent': '1032718',
                'strTimeline': 'Goal',
                'strPlayer': 'Lionel Messi',
                'intTime': '34'
            }]
        }

    @patch.object(LookupService, '_make_request')
    def test_get_event_tv(self, mock_request, lookup_service):
        mock_request.return_value = {
            'tv': [{
                'idEvent': '584911',
                'strChannel': 'ESPN',
                'strCountry': 'United States'
            }]
        }

        result = lookup_service.get_event_tv(584911)

        mock_request.assert_called_once_with('lookuptv.php?id=584911')
        assert result == {
            'tv': [{
                'idEvent': '584911',
                'strChannel': 'ESPN',
                'strCountry': 'United States'
            }]
        }
