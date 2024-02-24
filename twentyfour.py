import math

def trapez(func, a, b, N):
    f = getattr(math, func)
    step = (b - a) / N
    ans = 0
    for i in range(0, N):
        ans += (f(a + i*step) + f(a + (i + 1)*step))/2*step

    return round(ans, 8)



request = list(input().split())
print(trapez(request[0][5:], float(request[1]), float(request[2]), int(request[3])))

