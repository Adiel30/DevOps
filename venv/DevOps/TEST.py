import urllib.request, json
with urllib.request.urlopen( "https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=ultra&apiKey=33ab18c9aeb0d92f55f5") as url:
    data = json.loads(url.read().decode())
    print(data)
results = {'ILS_USD': 0.279826}
ILS_USD = results['ILS_USD']
print(ILS_USD)
currency_value = ILS_USD
print("Welcome to currency converter")
try:
    amount = float(input("Please enter an amount of Shekeles to convert:"))
    print("Result is: ",float(amount * currency_value))
    print("Thanks for using our currency converter")
except ValueError:
    print("Invalid Choice")