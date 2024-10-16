first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
if first == second and second == third:
    print("все 3 числа равны")
elif first == second or second == third or third == first:
    print("2 числа из введённых равны")
else:
    print('все введённые числа разные')