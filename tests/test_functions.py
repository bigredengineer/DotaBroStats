from dota_utils import functions


class TestBasicFunctions:
    def test_something(self):
        x = True
        assert x == 1

    def test_create_hero_lookup(self):
        hero_records = [
            {'id': 1, 'name': 'stark'},
            {'id': 2, 'name': 'banner'},
            {'id': 3, 'name': 'thor'}
        ]

        hero_lookup = functions.create_hero_lookup(hero_records)
        assert len(hero_lookup) == 3
        assert hero_lookup[3]['name'] == 'thor'
