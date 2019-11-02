import json
from typing import Dict, List
import os


MOCK_DATA = """
[{
    "address_components": [{
        "long_name": "28-15",
        "short_name": "28-15",
        "types": ["street_number"]
    }, {
        "long_name": "34th Street",
        "short_name": "34th St",
        "types": ["route"]
    }, {
        "long_name": "Long Island City",
        "short_name": "LIC",
        "types": ["neighborhood", "political"]
    }, {
        "long_name": "Queens",
        "short_name": "Queens",
        "types": ["political", "sublocality", "sublocality_level_1"]
    }, {
        "long_name": "Queens County",
        "short_name": "Queens County",
        "types": ["administrative_area_level_2", "political"]
    }, {
        "long_name": "New York",
        "short_name": "NY",
        "types": ["administrative_area_level_1", "political"]
    }, {
        "long_name": "United States",
        "short_name": "US",
        "types": ["country", "political"]
    }, {
        "long_name": "11103",
        "short_name": "11103",
        "types": ["postal_code"]
    }],
    "formatted_address": "28-15 34th St, Long Island City, NY 11103, USA",
    "postal": "11103",
    "geometry": {
        "location": {
            "lat": 40.7667831,
            "lng": -73.91779679999999
        },
        "location_type": "ROOFTOP",
        "viewport": {
            "northeast": {
                "lat": 40.76813208029149,
                "lng": -73.91644781970848
            },
            "southwest": {
                "lat": 40.76543411970849,
                "lng": -73.9191457802915
            }
        }
    },
    "place_id": "ChIJ_eoztkBfwokRJZ8i8DXMYfI",
    "plus_code": {
        "compound_code": "Q38J+PV New York, United States",
        "global_code": "87G8Q38J+PV"
    },
    "types": ["street_address"]
}]"""


def fetch_geocode(
    address, components=None, bounds=None, region=None, language=None
) -> List[Dict[str, any]]:

    # filepath = os.path.join(os.path.dirname(__file__), "sample-response-geocode.json")
    # with open(filepath) as f:
    #    return json.loads(f.read())
    return json.loads(MOCK_DATA)


# TODO fetch_reverse_geocode
