import requests

from dota_utils.functions import OpenDotaError


class DotaPlayerStats:
    """Class for collecting an individual player's stats by querying OpenDota APIs"""
    API_URL = "https://api.opendota.com/api"
    LOBBY_RANKED = 7  # OpenDota LobbyID for Ranked matches

    def __init__(self, open_id):
        self.open_id = open_id
        self.name = ''
        self._player_info = {}
        self._ranked_matches = []

    def get_player_info(self):
        if not self._player_info:
            self._populate_player_info()
        return self._player_info

    def get_matches(self):
        if not self._ranked_matches:
            self._populate_ranked_matches()
        return self._ranked_matches

    def _populate_player_info(self):
        """Simple function to get PlayerInfo from OpenDota and error check"""
        response = requests.get(f"{self.API_URL}/players/{self.open_id}/")

        if response.ok:
            self._player_info = response.json()
            try:
                self.name = self._player_info['profile']['personaname']
            except KeyError:
                print(f"DEBUG: Bad OpenDota PlayerData: {self._player_info}")
                raise KeyError("Unknown PlayerInfo returned from OpenDota. Cannot determine Player Name")
        else:
            raise OpenDotaError(response.status_code, response.text)

    def _populate_ranked_matches(self):
        """Simple function to get Ranked Matches from OpenDota and error check"""
        params = {'lobby_type': self.LOBBY_RANKED}
        response = requests.get(f"{self.API_URL}/players/{self.open_id}/matches", params=params)

        if response.ok:
            self._ranked_matches = response.json()
        else:
            raise OpenDotaError(response.status_code, response.text)
