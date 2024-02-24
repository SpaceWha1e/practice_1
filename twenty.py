ans, temp, n = 0e-06, 1 + 1e-06, 1
x = float(input())
while abs(temp) > 1e-06:
    temp = (-1)**(n - 1) * x**n / n
    ans += temp
    n += 1

print(round(ans, 8))
