# github link - https://github.com/KozhevnikovSpb/synergy_python.git

N = int(input("Введите количество значений массива: "))
listN = []

for n in range(N):
    listN.append(int(input("Введите значение занчение номер " + str(n) + ": ")))

print(listN)        # Выводим список в прямом порядке

listN.reverse()     # Переворачиваем список

print(listN)        # Выводим список в обратном порядке





