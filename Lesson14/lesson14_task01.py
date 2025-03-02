# github link - https://github.com/KozhevnikovSpb/synergy_python.git

def recurs(list_rec):
    if len(list_rec) <= 0:
        print("Конец списка.")
        return
    
    print(list_rec.pop(0))
    recurs(list_rec)
    

def main():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    recurs(my_list)


if __name__ == "__main__":
    main()
