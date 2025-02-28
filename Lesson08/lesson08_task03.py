# github link - https://github.com/KozhevnikovSpb/synergy_python.git

m = int(input("Введите массу, которую может выдержать лодка: "))
n = int(input("Введите количество рыбаков: "))
listN = []
listM = []
countM = 0

for a in range(1, n + 1):
    listN.append(int(input("Введите вес рыбака номер " + str(a) + " : ")))

listN.sort(reverse = True)

for i in range(len(listN)):
    minN = min(listN)
    if (listN[i] + min(listN) <= m) and (i != len(listN) - 1):
        listM.append([listN[i], min(listN)])
        listN[i] += m
        listN[listN.index(min(listN))] += m        
    else:
        if listN[i] > m:
            continue
        else:
            listM.append(listN[i])

#print(f"Комбинация пар рыбаков по весу в лодках {listM}.")
#print(f"Количество необходимых лодок для переправки рыбаков = {len(listM)}.")
print(len(listM))









