

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
