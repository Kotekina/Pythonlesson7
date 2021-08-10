"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
 с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        #str = '\n'
        ##for row in self.matr:
            #for el in row:
                #str += f'{el:>10}'
            #str += '\n'
        #return str
        return ('   \n'.join(['    '.join([str(row) for row in el]) for el in self.matr]))

    def __add__(self, other):
        add = []
        if len(self.matr) != len(other.matr):
            print('Размеры ваших мартиц не совпадают!')
            return
        for i in range(len(self.matr)):
            if len(self.matr[i]) != len(other.matr[i]):
                print('Размеры ваших мартиц не совпадают!')
                return
            row = []
            for j in range(len(self.matr[i])):
                row.append(self.matr[i][j] + other.matr[i][j])
            add.append(row)
        return  Matrix(add)

matr1 = Matrix([[2, 3, 5], [7, 8, 2], [3, 4, 7]])
matr2 = Matrix([[3, 1, 5], [2, 4, 2], [3, 7, 5]])
print(f'matr1 = \n{matr1}')
print(f'matr2 = \n{matr2}')
print(f'matr1+matr2 = \n{matr1 + matr2}')