melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455, 'Si': 1415, 'Be': 1287}
first, second = input().split()
print(melt.get(first) - melt.get(second))
