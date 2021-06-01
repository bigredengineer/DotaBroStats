import json
from mock import patch
import pytest

from dota_utils import player
from dota_utils.common import OpenDotaError, MockRequest
from dota_utils.player import DotaPlayerStats


class TestDotaPlayerStats:
    def test_basic(self):
        tony = DotaPlayerStats(11)
        assert tony.open_id == 11

    def test_player_info(self):
        dota_player = DotaPlayerStats(11)

        api_data = '{"tracked_until": "12345", "profile": {"name": "None", "personaname": "TonyStark", ' \
                   '"steamid": "9876"}}'
        with patch.object(player.requests, 'get', return_value=MockRequest(200, api_data)):
            player_info = dota_player.get_player_info()
            assert 'profile' in player_info
            assert player_info['profile']['personaname'] == 'TonyStark'

        # Don't reload data on 2nd call
        with patch.object(player.requests, 'get', return_value=MockRequest(200, '{"some_other": "data"}')):
            player_info = dota_player.get_player_info()
            assert 'profile' in player_info
            assert player_info['profile']['personaname'] == 'TonyStark'

        # Error mode checking
        with patch.object(player.requests, 'get', return_value=MockRequest(401, 'This is an error!')):
            dota_player = DotaPlayerStats(12)
            with pytest.raises(OpenDotaError, match="401.*an error"):
                dota_player.get_player_info()

        # Error: Profile missing from Player Data
        with patch.object(player.requests, 'get', return_value=MockRequest(200, '{"steamid": 12345}')):
            dota_player = DotaPlayerStats(13)
            with pytest.raises(KeyError, match="Unknown PlayerInfo"):
                dota_player.get_player_info()

    def test_match_info(self):
        dota_player = DotaPlayerStats(11)

        api_data = '[{"match_id": 12345, "lobby_type": 7},{"match_id": 23456, "lobby_type": 7}]'
        with patch.object(player.requests, 'get', return_value=MockRequest(200, api_data)):
            matches = dota_player.get_matches()
            assert len(matches) == 2
            assert 'match_id' in matches[0]

        # Don't reload data on 2nd call
        with patch.object(player.requests, 'get', return_value=MockRequest(200, '{"some_other": "data"}')):
            matches = dota_player.get_matches()
            assert len(matches) == 2
            assert 'match_id' in matches[0]

        # Error mode checking
        with patch.object(player.requests, 'get', return_value=MockRequest(401, 'This is an error!')):
            dota_player = DotaPlayerStats(12)
            with pytest.raises(OpenDotaError, match="401.*an error"):
                dota_player.get_matches()
