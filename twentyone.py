a = list(map(int, input().split()))
max_speed = 0
for i in range(1, len(a)):
    max_speed = max(a[i] - a[i - 1], max_speed)
print(max_speed * 100)

