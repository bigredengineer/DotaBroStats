import requests
import json

from dota_utils.common import OpenDotaError


def create_hero_lookup(hero_records: list):
    """
    Convert input hero list to a dictionary based on 'hero_id'
    :param hero_records:  List of the Hero info data structure returned by OpenDotaApi
    :return: dictionary of hero records indexed by hero ID
    """
    lookup = {}
    for rec in hero_records:
        lookup[rec['id']] = rec

    return lookup


def get_heroes():
    """Create a dictionary based on hero id of all Dota heros"""
    r = requests.get("https://api.opendota.com/api/heroes")
    if r.ok:
        hero_recs = create_hero_lookup(r.json())
        return hero_recs
    else:
        raise OpenDotaError(r.status_code, r.text)
