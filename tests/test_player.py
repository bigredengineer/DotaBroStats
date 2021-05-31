from dota_utils.player import DotaPlayerStats


class TestDotaPlayerStats:
    def test_basic(self):
        tony = DotaPlayerStats(11)
        assert tony.open_id == 11
