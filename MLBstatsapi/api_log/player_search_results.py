# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Request (4)
    # GET http://lookup-service-prod.mlb.com/json/named.search_player_all.bam

    try:
        response = requests.get(
            url="http://lookup-service-prod.mlb.com/json/named.search_player_all.bam",
            params={
                "sport_code": "'mlb'",
                "active_sw": "'Y'",
                "name_part": "'young%'",
                "search_player_all.col_ex": "player_id",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


