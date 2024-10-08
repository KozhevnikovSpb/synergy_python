# github link - https://github.com/KozhevnikovSpb/synergy_python.git

str01 = input("Введите слово: ")
palindrome = True


for i in range(len(str01) // 2):
    if str01[i] != str01[len(str01) - 1 - i]:
        palindrome = False
        break    

if palindrome:
    print(f'yes')
else:
    print(f'no')




