# github link - https://github.com/KozhevnikovSpb/synergy_python.git

X = int(input("Введите натуральное число X: "))

if X == 1:
    schet = 1
else:
    schet = 2                                            # Счетчик начинается с двух, т.к. число точно делится на 1 и на само себя
#    for n in range(2, int(X / 2) + 1):                  # Все что больше X / 2, не рассматривается т.к. там небудет натуральных делителей
#        if X % n == 0:
#            schet += 1                                  # Большие числа достаточно долго считает
    for n in range(2, int(X ** 0.5) + 1):                # Способ перебора чисел до корня из числа X.
       if X % n == 0:
           schet += 1
           if n != X // n:
               schet += 1

print("Количество натуральных делителей числа " + str(X) + " = " + str(schet))