import requests

app_access_token = 'MLY|7717967788302964|a7ba980b29ff82c24ba19f12d872da0d' # create your access token at https://mapillary.com/developer
image_id = '259387669304602'
url = 'https://graph.mapillary.com/{}/detections?fields=id,value,created_at&access_token={}'.format(image_id,app_access_token)
# or instead of adding it to the url, add the token in headers (strongly recommended for user tokens)
headers = { "Authorization" : "OAuth {}".format(app_access_token) }
response = requests.get(url, headers)
data = response.json()

print(data)