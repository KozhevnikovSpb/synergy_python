# github link - https://github.com/KozhevnikovSpb/synergy_python.git
str01 = input("Введите слово маленькими латинскими буквами: ")

a = str01.count('a')
e = str01.count('e')
i = str01.count('i')
o = str01.count('o')
u = str01.count('u')

sumGlas = a + e + i + o + u
sumSogl = len(str01) - sumGlas

print("Гласных букв =", sumGlas, "Согласных букв =", sumSogl)

if a == 0:
    print("a - False")
if e == 0:
    print("e - False")
if i == 0:
    print("i - False")
if o == 0:
    print("o - False")
if u == 0:
    print("u - False")

if (a == 0) or (e == 0) or (i == 0) or (o == 0) or (u == 0):
    print("False")