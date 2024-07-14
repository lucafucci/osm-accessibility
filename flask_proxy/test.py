from flask import Flask, jsonify, request
from flask_cors import CORS

import requests



if __name__ == '__main__':
    API_KEY = '1d7cfe17d545fb54e23d084b84316e68ff8cbc7a'

    asset_id = 'ahE3SdWtGpcDgcSD7HoHFr'
    GEOJSON_URL = f'https://kf.kobotoolbox.org/api/v2/assets/{asset_id}/data.json'

    headers = {
        'Authorization': f'Token {API_KEY}'
    }
    response = requests.get(GEOJSON_URL, headers=headers)
    print(response.json())
