import math


def matrix_create(row, column):  # процедура расширяющая массивы
    a = []
    if column > 1:  # если не вектор
        for i in range(row):
            a.append([])
            for j in range(column):
                a[i].append([])
    else:
        for i in range(column):
            a.append([])
    return a


def matrix_init(a):  # процедура ввода массива
    print("Enter matrix value:")
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = float(input())
    return a


def matrix_print(a):
    for r in a:
        print(r)


def choose_matrix(a, b, c):
    print("Which matrix would you like to choose?")
    cycling = 1
    while cycling == 1:
        matrix = input().upper()
        if matrix == 'A':
            print("You have chosen matrix A")
            c = a
            cycling = 0
        elif matrix == 'B':
            print("You have chosen matrix B")
            c = b
            cycling = 0
        else:
            print('Unknown matrix')
            print('Try again')
            continue
    return c


class Tmatrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = matrix_create(self.row, self.column)  # расширяем массив
        self.matrix = matrix_init(self.matrix)  # вводим матрицу
        matrix_print(self.matrix)


class lin_alg:
    def __init__(self, a, b):
        self.matrix_1 = a
        self.matrix_2 = b
        self.a = a.matrix  # матрица a
        self.b = b.matrix  # матрица b
        self.column_a = a.column
        self.row_a = a.row
        self.column_b = b.column
        self.row_b = b.row
        self.column_c = 0
        self.row_c = 0
        self.c = []

    def size_check(self, func):
        result = 0
        if (self.row_a == self.row_b) and (self.column_a == self.column_b) and func == 1:
            result = 1  # единица если размеры матрицы полностью совпадают и для случая с суммированием и умножением
            self.column_c = self.column_a
            self.row_c = self.row_a
        elif (self.column_a == self.row_b) and func == 2:
            result = 2  # для случая перемножения матриц
            self.row_c = self.row_a
            self.column_c = self.column_b
        elif ((self.row_a == 1) and (self.row_b == 1) and (self.column_a == self.column_b)) and func == 3:
            result = 3  # разрешение для векторной алгебры проверка на то, что введеные матрицы вектора
        elif (self.column_a != self.column_b) and func == 3:
            result = 4  # вектора разной размерности

        return result

    def sum(self):
        func = 1
        check_size = self.size_check(func)
        if check_size == 1:
            self.c = matrix_create(self.row_a, self.column_a)
            for i in range(len(self.c)):
                for j in range(len(self.c[i])):
                    self.c[i][j] = self.a[i][j] + self.b[i][j]
            print("sum of a and b:")
            matrix_print(self.c)
        else:
            print("Different sizes!!")
        return self.c

    def mult(self):
        func = 2
        check_size = self.size_check(func)
        if check_size == 2:
            self.c = matrix_create(self.row_a, self.column_b)
            for i in range(len(self.a)):
                for j in range(len(self.b[0])):
                    self.c[i][j] = 0
                    for k in range(len(self.a[i])):
                        self.c[i][j] += self.a[i][k] * self.b[k][j]
            print("composition of a and b:")
            matrix_print(self.c)
        else:
            print("Different sizes!")
        return self.c

    def mult_mat_number(self):
        self.c = choose_matrix(self.a, self.b, self.c)
        print('Enter the number:')
        n = float(input())
        for i in range(len(self.c)):
            for j in range(len(self.c[i])):
                self.c[i][j] = self.c[i][j] * n
        matrix_print(self.c)

    def transparent(self):
        self.a = choose_matrix(self.a, self.b, self.c)
        column = 0
        row = 0
        for i in range(len(self.a)):  # количество строк в матрице
            row += 1
        for i in range(1):
            for j in range(len(self.a[i])):  # проходим по одной строке, чтобы узнать размер
                column += 1  # количество столбцов в матрице
        self.c = matrix_create(column, row)
        for i in range(column):
            for j in range(row):
                self.c[i][j] = self.a[j][i]
        print("Transparent matrix: ")
        matrix_print(self.c)

    def scalar_product(self):
        func = 3
        check_size = self.size_check(func)
        if check_size == 3:
            number = 0
            for i in range(len(self.a)):
                for j in range(len(self.a[i])):
                    number += self.a[i][j] * self.b[i][j]
            print("scalar product of A an B: %s" % number)
        elif self.row_a != 1:
            print("Matrix a is not a vector")
        elif self.row_b != 1:
            print("Matrix b is not a vector")
        elif check_size == 4:
            print("Different sizes of vectors")

    def len_vec(self):
        self.c = choose_matrix(self.matrix_1, self.matrix_2, self.c)
        length = 0
        column = 0
        row = 0
        for i in range(len(self.c)):  # количество строк в матрице
            row += 1
        for i in range(1):
            for j in range(len(self.c[i])):  # проходим по одной строке, чтобы узнать размер
                column += 1  # количество столбцов в матрице
        if row == 1:
            for i in range(len(self.c[0])):
                length += self.c[i] * self.c[i]
            length = math.sqrt(length)
        else:
            print('Not vector!')
        return length
