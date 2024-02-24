def calculate(args):
    ans = 1
    for x in args:
        ans *= x
    return ans


print(calculate(list(map(int, input().split()))))
