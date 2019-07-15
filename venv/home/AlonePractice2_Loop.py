n = 4
while n < 100:
    m = 4
    while (m <= (n/m)):
        if not (n % m): break
        m = m + 1
    if (m > n/m): print(n, "it is a prime ")
    n = n + 1
print('its done')





b = 17
x = 5

print(b % x)