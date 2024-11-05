# Вариант 1: перебор всех чисел.
number = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

for t in number:
    list_ = []
    result = ""
    for m in range(1, t + 1):
        for r in range(3, t + 1):
            if t % r == 0:
                if r not in list_:
                    list_.append(r)
                else:
                    continue
    for v in range(1, t):
        for r in range(1, t):
            for p in list_:
                if v + r == p and v < r:
                    result = result + str(v) + str(r)
                else:
                    continue
    print(f"{t} - {result}")

# Вариант 2: С вводом числа от 3 до 20 вручную.
print("Введите число от 3 до 20")
number = (int(input()))

result = ""
list_ = []
for m in range(1, number + 1):
    for r in range(3, number + 1):
        if number % r == 0:
            if r not in list_:
                list_.append(r)
            else:
                continue
for v in range(1, number):
    for r in range(1, number):
        for p in list_:
            if v + r == p and v < r:
                result = result + str(v) + str(r)
            else:
                continue

print(result)
