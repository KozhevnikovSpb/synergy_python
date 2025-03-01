# github link - https://github.com/KozhevnikovSpb/synergy_python.git

import collections

def create():
    # Функция создания питомца
    if len(pets) == 0:
        num = 1
    else:
        num = collections.deque(pets, maxlen=1)[0] + 1

    name = input("Введите имя питомца: ")           # Вводим кличку питомца        
    pets[num] = {name: {"Вид питомца": input("Введите вид питомца: "), "Возраст питомца": int(input("Укажите возраст питомца: ")), "Имя владельца": input("Укажите имя владельца: ")}}
    print()

def get_pet(ID):
    # Получение питомца из базы по индексу, возврат ошибки если такого питомца нет
    if ID in pets.keys():
        petsD = pets[ID]    
    else:
       petsD = False
       print("Питомца с таким индексом нет в списке.")

    return petsD

def get_suffix(age):
    # Функция получения суффикса год, года, лет
    if age % 100 in (11, 12, 13, 14):
        return "лет"            
    elif age % 10 == 1:
        return "год"
    elif age % 10 in (2, 3, 4):
        return "года"
    else:
        return "лет"

def read(ID):
    # Функция вывода питомцев    
    pet = get_pet(ID)
    if pet is False:
        return False

    namePet = next(iter(pet))
    typePet = pet[namePet]["Вид питомца"]
    age = pet[namePet]["Возраст питомца"]
    years = get_suffix(age)
    owner = pet[namePet]["Имя владельца"]

    print(f"Это {typePet} по кличке \"{namePet}\". Возраст питомца {age} {years}. Имя владельца: {owner}.")

def update(ID):
    # Функция обновления записи в базе данных
    if get_pet(ID) is False:
        return 0

    namePet = next(iter(pets[ID]))
    print("Если необходимо изменить данные, введите новое значени или нажмите ENTER для пропуска.")

    newPetName = input("Кличка питомца " + namePet + " - ")
    if newPetName:
        pets[ID][newPetName] = pets[ID].pop(namePet)
        namePet = newPetName

    newType = input("Вид питомца " + pets[ID][namePet]["Вид питомца"] + " - ")
    if newType:
        pets[ID][namePet]["Вид питомца"] = newType

    newAge = int(input("Возраст питомца " + str(pets[ID][namePet]["Возраст питомца"]) + " - "))
    if newAge:
        pets[ID][namePet]["Возраст питомца"] = newAge

    newOwner = input("Владелец питомца " + pets[ID][namePet]["Имя владельца"] + " - ")
    if newOwner:
        pets[ID][namePet]["Имя владельца"] = newOwner
        
def delete(ID):
    # Функция удаления записи из базы данных
    if get_pet(ID) is False:
        return 0

    delPet = pets.pop(ID)
    print(f"Запись {delPet} удалена из базы")
    
def list():   
    # Функция вывода всего списка питомцев из базы данных
    for pet in pets:        
        print(f"Номер {pet}. ", end="")
        read(pet)


def main():
    global pets 
    pets = dict()                             # Создаем пустой словарь

    while (True):
        # Меню выбора команды
        cmd = input("Введите команду: ")
        if cmd == "stop":
            break
        elif cmd == "create":
            create()
        elif cmd == "read":
            read(int(input("Введите номер записи для чтения: ")))
        elif cmd == "update":
            update(int(input("Введите номер записи для обновления: ")))
        elif cmd == "delete":
            delete(int(input("Введите номер записи для удаления: ")))
        elif cmd == "list":
            list()
        else:
            print("Вы ввели не верную команду.\n")


if __name__ == '__main__':
    main()



