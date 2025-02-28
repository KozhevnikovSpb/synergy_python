# github link - https://github.com/KozhevnikovSpb/synergy_python.git

# Задаем словарь с помощью генератора, используя range в обратном порядке до -5 включительно.
num = dict((k, k**k) for k in range(10, -6, -1))
print(num)