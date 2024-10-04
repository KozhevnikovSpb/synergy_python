# github link - https://github.com/KozhevnikovSpb/synergy_python.git
X = int(input("Введите минимальную сумму инвестиций: "))
A = int(input("Введите сумму инвестиций Майкла: "))
B = int(input("Введите сумму инвестиций Ивана: "))

if (A >= X) and (B >= X):
    print(2)
elif (A >= X):
    print("Mike")
elif (B >= X):
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)