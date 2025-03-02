# github link - https://github.com/KozhevnikovSpb/synergy_python.git

class Cassa(object):
    """ Родительский класс Касса."""
    cash = 0        # Количество денег в кассе по умолчанию

    def __init__(self):
        """ Конструктор родительского класса. Создаем пустую кассу."""
    
    def top_up(self, cash):
        """ Метод пополнения наличых в кассе."""
        self.cash += cash

    def take_away(self, cash):
        """ Метод выдачи денег из кассы."""
        remnant = self.cash - cash
        if remnant < 0:
            print("В кассе недостаточно денежных средств для выдачи.")
        else:
            self.cash -= cash
            
    def count_1000(self):
        """ Метод вывода целых тысяч в кассе. """
        print(f"В кассе есть {self.cash // 1000} целых тысяч.")

    def remmant_cash(self):
        """ Метод выводит остаток денежных средств в кассе."""
        print(f"В кассе осталось {self.cash} денег.")
        

def main():
    myCassa = Cassa()
    myCassa.top_up(150)
    myCassa.remmant_cash()
    myCassa.take_away(200)
    myCassa.take_away(50)
    myCassa.remmant_cash()
    myCassa.top_up(3000)
    myCassa.remmant_cash()
    myCassa.count_1000()
    

if __name__ == "__main__":
    main()
