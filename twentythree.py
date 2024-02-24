def my_filter(a):
    s = ""
    for i in range(len(a)):
        s += str(a[i] * 10) + ' '
    return s[0:-1]


print(my_filter(list(map(int, input().split()))))

