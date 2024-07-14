from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/data')
def get_geojson_data():
    asset_id = request.args.get('asset_id')
    include_attachments = request.args.get('include_attachments', 'no').lower() == 'true'
    
    if not asset_id:
        return jsonify({"error": "Missing asset_id parameter"}), 400

    GEOJSON_URL = f'https://kf.kobotoolbox.org/api/v2/assets/{asset_id}/data.geojson'
    JSON_URL = f'https://kf.kobotoolbox.org/api/v2/assets/{asset_id}/data.json'

    # Fetch the geojson data
    response_geojson = requests.get(GEOJSON_URL)
    if response_geojson.status_code != 200:
        return jsonify({"error": "Failed to fetch geojson data"}), response_geojson.status_code

    geojson_data = response_geojson.json()

    if include_attachments:
        # Fetch the json data with attachments
        response_json = requests.get(JSON_URL)
        if response_json.status_code != 200:
            return jsonify({"error": "Failed to fetch json data"}), response_json.status_code

        json_data = response_json.json()

        # Create a map of filename to download_url
        attachments_map = {}
        for result in json_data['results']:
            for attachment in result['_attachments']:
                filename = attachment['filename'].split('/')[-1]
                attachments_map[filename] = attachment['download_url']

        # Add download_url to geojson features
        for feature in geojson_data['features']:
            properties = feature['properties']
            keys_to_update = []
            for key, value in properties.items():
                if isinstance(value, str) and value in attachments_map:
                    keys_to_update.append((key, attachments_map[value]))

            for key, download_url in keys_to_update:
                properties['download_url'] = download_url

    return jsonify(geojson_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
