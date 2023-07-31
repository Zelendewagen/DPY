# Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц
class Matrix:
    def __init__(self, matrix):
        """
        Конструктор класса
        :param matrix: Двумерный список
        """
        self.matrix = matrix

    def print_matrix(self):
        """Выводим матрицу на экран"""
        for row in self.matrix:
            print(*row)

    def __eq__(self, other):
        if self.matrix != other.matrix:
            return False
        return True

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Матрица неправильного размера")
        for row in range(len(self.matrix)):
            if len(self.matrix[row]) != len(other.matrix[row]):
                raise ValueError("Матрица неправильного размера")
        new_matrix = []
        for row_self, row_other in zip(self.matrix, other.matrix):
            new_matrix.append([*map(lambda x: sum(x), zip(row_self, row_other))])
        return Matrix(new_matrix)

    def __mul__(self, other):
        if len(self.matrix[0]) == len(other.matrix):
            new_matrix = []
            for row_self in self.matrix:
                temp = []
                for col_other in zip(*other.matrix):
                    temp.append(sum(map(lambda x: x[0] * x[1], zip(row_self, col_other))))
                new_matrix.append(temp)
            return Matrix(new_matrix)
        raise ValueError("Матрица неправильного размера")


m1 = Matrix(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]])

m2 = Matrix(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]])

m3 = m1 + m2

m3.print_matrix()

