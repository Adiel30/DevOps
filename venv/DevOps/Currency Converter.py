import urllib.request, json
with urllib.request.urlopen(
        ":=ILS_USD&compact=ultra&apiKey=33ab18c9aeb0d92f55f5") as convert:
    currencyRate = json.loads(convert.read().decode())
print(currencyRate)
ILS_USD = currencyRate['ILS_USD']
currencyValue = ILS_USD
try:
    shekel = float(input('Enter Shekel Value:'))
    print('Result is: ',float(shekel * currencyValue))
    print("Thanks for using our currency converter")
except ValueError:
    print("Invalid Choice")
