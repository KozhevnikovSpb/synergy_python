# github link - https://github.com/KozhevnikovSpb/synergy_python.git
print("Введите пятизначное число: ", end='')
chislo = int(input())
edinici = chislo % 10               # вычисляем количество единиц в числе
desiatki = chislo // 10 % 10        # вычисляем количество десятков в числе
sotni = chislo // 100 % 10          # вычисляем количество сотен в числе
tisiachi = chislo // 1000 % 10      # вычисляем количество тысяч в числе
desTisiach = chislo // 10000 % 10   # вычисляем количество десотк тысяч в числе
otvet = desiatki ** edinici * sotni / (desTisiach - tisiachi)
print(otvet)

