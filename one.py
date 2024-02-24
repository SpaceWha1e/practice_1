room = int(input())
if 0 < room < 33:
    print("Подъезд: ", (room - 1) // 8 + 1, "\nЭтаж: ", room % 8 + (not (room % 8)) * 8)
else:
    print("Квартиры не существует")
