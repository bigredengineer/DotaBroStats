import json
from mock import patch
import pytest

from dota_utils.common import OpenDotaError, MockRequest
from dota_utils import functions


class TestBasicFunctions:
    def test_something(self):
        x = True
        assert x == 1

    def test_get_heroes(self):
        hero_records = [
            {'id': 1, 'name': 'stark'},
            {'id': 2, 'name': 'banner'},
            {'id': 3, 'name': 'thor'}
        ]

        # Basic test of underlying lookup
        api_data = json.dumps(hero_records)
        with patch.object(functions.requests, "get", return_value=MockRequest(200, api_data)):
            hero_lookup = functions.get_heroes()
            assert len(hero_lookup) == 3
            assert hero_lookup[3]['name'] == 'thor'

        # Error checking
        with patch.object(functions.requests, "get", return_value=MockRequest(401, 'This is an error!')):
            with pytest.raises(OpenDotaError, match='401.*an error'):
                functions.get_heroes()
