# github link - https://github.com/KozhevnikovSpb/synergy_python.git
print("Введите через пробел длины сторон прямоугольника. После завершения ввода нажмите клавишу Enter")
a, b = map(float, input().split())
p = (a + b) * 2                                             # вычисляем периметр
s = a * b                                                   # вычисляем площадь

print("Периметр прямоугольника =", p)
print("Площадь прямоугольника =", s)

