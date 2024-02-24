x, y = map(float, input().split())
if 1 <= (x - 1)**2 + y**2 <= 2**2:
    print("yes", end=' ')
else:
    print("no", end=' ')

if abs(x - 4) < 2 and abs(y - 2) < 3:
    print("yes")
else:
    print("no")
