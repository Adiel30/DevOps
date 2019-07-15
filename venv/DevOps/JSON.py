import urllib.request, json

# Opening a web request
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=ultra&apiKey=33ab18c9aeb0d92f55f5")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request
print(data)
# Parsing results
#results = data['results']
#print(results)
ILS_USD = data['ILS_USD']
val = ILS_USD['0.279826']
print(val)

