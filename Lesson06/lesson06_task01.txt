# github link - https://github.com/KozhevnikovSpb/synergy_python.git

N = int(input("Введите число N: "))
schet = 0

for n in range(N):
    a = int(input("Введите значение числа " + str(n + 1) + ": "))
    if a == 0:
        schet += 1

print("Нулевых значений чисел =", schet)
