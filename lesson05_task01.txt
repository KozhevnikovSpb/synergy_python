# github link - https://github.com/KozhevnikovSpb/synergy_python.git
chislo = int(input("Введите целое четное число: "))

if chislo % 2 == 0:
    if chislo > 0:
        print("Положительное четное число.")
    elif chislo < 0:
        print("Отрицательное четное число.")
    else:
        print("Нулевое число.")
else:
    print("Число не является четным!")