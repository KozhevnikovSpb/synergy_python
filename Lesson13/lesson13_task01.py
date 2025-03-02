# github link - https://github.com/KozhevnikovSpb/synergy_python.git
# Сделал через классы, т.к. это удобнее и эту тему я уже изучил.
import random

class Matrix():
    """ Класс для работы с двумерным массивом - матрицей"""
    def __init__(self):
        """ Конструктор класса, создает пустую матрицу."""        
        self.data = []
            
    def create_matrix(self, rows, cols, start=-20, end=30):
        """ Метод заполнения матрицы. В метод передается размер матрицы и начальный и конечный range для заполнения случайными данными."""
        self.data = [[random.randint(start, end) for cl in range(cols)] for rw in range(rows)]

    def summ_matrix(self, obj):
        """ Метод суммирования матриц. Метод берет матрицу текущего объекта и суммирует с матрицей передаваемого объекта. Матрицы должны быть одинакового размера."""
        lenData = len(self.data) * len(self.data[0])
        lenObj = len(obj.data) * len(obj.data[0])

        if lenData != lenObj:
            print("Матрицы разного размера.")
            return False
        
        result = []

        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + obj.data[i][j])
            result.append(row)

        return result  
    
    def print_matrix(self):
        """ Метод вывода объекта матрицы на печать. """
        for row in self.data:
            print(row)
        print()


def main():
    # Создаем объекты матриц
    matrix_01 = Matrix()
    matrix_02 = Matrix()    

    # Заполняем матрицы и вводим на печать
    matrix_01.create_matrix(3, 5)
    matrix_01.print_matrix()
    matrix_02.create_matrix(3, 5)
    matrix_02.print_matrix()

    # Получаем матрицу 3, путем сложения матрицы 1 и матрицы 2. Матрица 3 не является объектом, а явялется списком.
    matrix_03 = matrix_01.summ_matrix(matrix_02)
    # Выводим список на печать
    if matrix_03 != False:
        for row in matrix_03:
            print(row)


if __name__ == "__main__":
    main()