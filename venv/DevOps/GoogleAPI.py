import urllib.request, json
with urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Jerusalem&key=AIzaSyB-Z0RBleTXb7JHLx6QhSANPeTiOkMyKj4")as places:
    googlePlaces = json.loads(places.read().decode())
    print(googlePlaces)
results = googlePlaces['results']
result = results[0]
geometry = result['geometry']
location = geometry['location']
latitude = location['lat']
longitude = location['lng']

print('The Latitude is ',latitude, 'The Longitude is ', longitude)


