melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}
for x in melt.keys():
    if x.find('O') > 0:
        print(melt.get(x), end = ' ')
