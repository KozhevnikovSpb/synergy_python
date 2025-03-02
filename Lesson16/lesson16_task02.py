# github link - https://github.com/KozhevnikovSpb/synergy_python.git

class Turtle(object):
    """ Класс черепахи."""
    x = 0   # Позиция X
    y = 0   # Позиция Y
    s = 1   # Количество клеток на которые черепашка перемащается за ход

    def __init__(self):
        """ Конструктор родительского класса. Создаем черепашку со значениями по умолчанию."""
    
    def go_up(self):
        """ Метод передвиагет черепашку вверх на s клеток."""
        self.y += self.s

    def go_down(self):
        """ Метод передвигает черепашку вниз на s клеток."""
        self.y -= self.s
     
    def go_left(self):
        """ Метод передвигает черепашку влево на s клеток."""
        self.x -= self.s

    def go_right(self):
        """ Метод передвигает черепашку вправо на s клеток."""
        self.x += self.s

    def evolve(self):
        """ Увеличивает s на +1."""
        self.s += 1

    def degrade(self):
        """ Уменьшает s на -1."""
        if self.s > 0:
            self.s -= 1
        else:
            print("Ошибка!")

    def count_moves(self, _x, _y):
        """ Метод возвращает минимальное количество действий, за которое черепашка сможет добраться до _x и _y."""
        deltaX = abs(_x - self.x)
        deltaY = abs(_y - self.y)

        # При расчете учитываем, что черепашка двигается только на целое количество шагов
        movesX = deltaX // self.s + (1 if deltaX % self.s else 0)
        movesY = deltaY // self.s + (1 if deltaY % self.s else 0)
        result = movesX + movesY

        print(f"Минимальное количество шагов = {result}.")


def main():
    my_turtle = Turtle()
    my_turtle.count_moves(3, 4)
        

if __name__ == "__main__":
    main()
