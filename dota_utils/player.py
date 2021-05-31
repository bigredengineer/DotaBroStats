import requests


class DotaPlayerStats:
    """Class for collecting an individual player's stats by querying OpenDota APIs"""
    API_URL = "https://api.opendota.com/api"

    def __init__(self, open_id):
        self.open_id = open_id
        self.player_info = {}
        self.ranked_matches = []
