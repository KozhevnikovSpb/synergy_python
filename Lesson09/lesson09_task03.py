# github link - https://github.com/KozhevnikovSpb/synergy_python.git

listN = input("Введите последовательность чисел через пробел: ").split()     # Задаем последовательность чисел

# Проходим по действующем списку и выводим YES, в случае если число ранее встречалось
setN = set()                                                                 # Задаем пустое множество для добавления уникальных значений
for n in listN:
    print(str(n) + " - YES" if n in setN else str(n) + " - NO")
    setN.add(n)