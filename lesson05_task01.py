# github link - https://github.com/KozhevnikovSpb/synergy_python.git
print("Введите целое четное число: ", end='')
chislo = int(input())

if chislo % 2 == 0:
    if chislo > 0:
        print("Положительное четное число.")
    if chislo < 0:
        print("Отрицательное четное число.")
    else:
        print("Нулевое число.")
else:
    print("Число не является четным!")