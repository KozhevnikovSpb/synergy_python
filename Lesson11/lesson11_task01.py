# github link - https://github.com/KozhevnikovSpb/synergy_python.git

def factorial(n):
# Функция поиска факториала от числа
    if (n == 0) or (n == 1):
        factN = 1
    else:
        factN  = 1    
        for f in range(1, n + 1):
            factN *= f

    return(factN)


n = factorial(int(input("Введите натурально положительное число: ")))
listF = list()

for f in range(n, 0, -1):                   # Создаем список факториалов
    listF.append(factorial(f))

print(listF)

