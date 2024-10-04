# github link - https://github.com/KozhevnikovSpb/synergy_python.git

A, B = map(int, input("Введите целые числа A и B через пробел: ").split())
n = A

while n <= B:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1

print()

