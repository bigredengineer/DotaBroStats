import pprint
import time

import requests

from dota_utils import functions
from dota_utils.player import DotaPlayerStats

LOBBY_RANKED = 7

# ID's found manually on opendota.com
bigred_steamid = 76561197999367273
bigred_openid = 39101545
bro_openid = 252713525
aj_openid = 157308372
mike_openid = 193425438
base_url = "https://api.opendota.com/api"

# Gather Player Data
url = f"{base_url}/players/{bigred_openid}/"
print(f"URL: {url}")
r = requests.get(url)
bigred_info = r.json()
pprint.pprint(bigred_info)

start_players = time.perf_counter()
bro_info = requests.get(f"{base_url}/players/{bro_openid}/").json()
aj_info = requests.get(f"{base_url}/players/{aj_openid}").json()
mike_info = requests.get(f"{base_url}/players/{mike_openid}").json()
end_players = time.perf_counter()
print(f"Gathering Player Info Took: {end_players - start_players: .2f}s")
# pprint.pprint(mike_info)

# Get the list of Lifetime matches
r = requests.get(f"https://api.opendota.com/api/players/{bigred_openid}/matches")
bigred_match_info = r.json()
end_matches = time.perf_counter()
print(f"BigRed Match Count: {len(bigred_match_info)} ({len(r.json())}) [Took: {end_matches - end_players: .2f}s]")

# Load Hero data to map Hero IDs
r = requests.get("https://api.opendota.com/api/heroes")
hero_recs = r.json()
hero_info = functions.create_hero_lookup(hero_recs)
end_heroes = time.perf_counter()
print(f"Loaded {len(hero_info)} Hero Info [Took: {end_heroes - end_matches}s]")

print("Most Recent BigRed Match: ")
latest_match = bigred_match_info[0]
latest_hero = hero_info[latest_match['hero_id']]['localized_name']
pprint.pprint(latest_match)
print(f"Most Recent BigRed Hero: {latest_hero} "
      f"(ID: {latest_match['hero_id']})")
print(f"Total Time: {time.perf_counter() - start_players: .2f}s")
