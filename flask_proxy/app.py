from flask import Flask, jsonify, request
from flask_cors import CORS

import requests

app = Flask(__name__)
CORS(app)

API_KEY = '1d7cfe17d545fb54e23d084b84316e68ff8cbc7a'


@app.route('/test')
def get_test_geojson():
    asset_id = 'ahE3SdWtGpcDgcSD7HoHFr'
    GEOJSON_URL = f'https://kf.kobotoolbox.org/api/v2/assets/{asset_id}/data.geojson'

    headers = {
        'Authorization': f'Token {API_KEY}'
    }
    response = requests.get(GEOJSON_URL, headers=headers)
    return jsonify(response.json())


@app.route('/accessibility')
def get_accessibility_geojson():
    asset_id = 'aKoL7iVihKi5wPMHniZBqN'
    GEOJSON_URL = f'https://kf.kobotoolbox.org/api/v2/assets/{asset_id}/data.geojson'

    headers = {
        'Authorization': f'Token {API_KEY}'
    }
    response = requests.get(GEOJSON_URL, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True,port=5000)