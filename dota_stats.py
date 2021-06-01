import pprint
import time

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

# Player Objects
bigred_player = DotaPlayerStats(bigred_openid)
bro_player = DotaPlayerStats(bro_openid)
aj_player = DotaPlayerStats(aj_openid)
mike_player = DotaPlayerStats(mike_openid)

# Gather Player Data
start_players = time.perf_counter()
bigred_info = bigred_player.get_player_info()
pprint.pprint(bigred_info)

bro_info = bro_player.get_player_info()
aj_info = aj_player.get_player_info()
mike_info = mike_player.get_player_info()
end_players = time.perf_counter()
print(f"Gathering Player Info Took: {end_players - start_players: .2f}s")
# pprint.pprint(mike_info)

# Get the list of Lifetime matches
bigred_match_info = bigred_player.get_matches()
end_matches = time.perf_counter()
print(f"{bigred_player.name} Match Count: {len(bigred_match_info)} "
      f"[Took: {end_matches - end_players: .2f}s]")

# Load Hero data to map Hero IDs
hero_info = functions.get_heroes()
end_heroes = time.perf_counter()
print(f"Loaded {len(hero_info)} Hero Info [Took: {end_heroes - end_matches: .2f}s]")

print("Most Recent BigRed Match: ")
latest_match = bigred_match_info[0]
latest_hero = hero_info[latest_match['hero_id']]['localized_name']
pprint.pprint(latest_match)
print(f"Most Recent BigRed Hero: {latest_hero} "
      f"(ID: {latest_match['hero_id']})")
print(f"Total Time: {time.perf_counter() - start_players: .2f}s")
