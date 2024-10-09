# github link - https://github.com/KozhevnikovSpb/synergy_python.git

N = int(input("Введите количество значений массива: "))
print("Введите в строчку через пробел значения массива: ", end='')
listN = [int(n) for n in input().split()]

listN.append(listN[0])      # Добавляет первый элемент в конец
listN.remove(listN[0])      # Удаляет из списка первый элемент, все элементы сдвигаются влево

print(listN)






