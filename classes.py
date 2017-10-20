import math


def matrix_create(row, column):  # процедура расширяющая массивы
    a = []
    if column > 0:  # если не вектор
        for i in range(row):
            a.append([])
            for j in range(column):
                a[i].append([])
    else:
        for i in range(column):
            a.append([])
    return a


def vec_create(row):
    a = []
    for i in range(row):
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


def choose_matrix(a, b):
    c = Tmatrix
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


def checkmult(a, b):
    column_b = 0
    row_a = 0
    for i in range(len(a)):  # количество строк в матрице
        row_a += 1
    for i in range(1):
        for j in range(len(b[i])):  # проходим по одной строке, чтобы узнать размер
            column_b += 1  # количество столбцов в матрице
    c = matrix_create(row_a, column_b)
    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i][j] = 0
            for k in range(len(a[i])):
                c[i][j] += a[i][k] * b[k][j]
    print("composition of a and b:")
    matrix_print(c)
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
        if (self.row_a == self.row_b) and (self.column_a == self.column_b) and (func == 1 or func == 3):
            result = 1  # единица если размеры матрицы полностью совпадают и для случая с суммированием и умножением
            self.column_c = self.column_a
            self.row_c = self.row_a
        elif (self.column_a == self.row_b) and func == 2:
            result = 2  # для случая перемножения матриц
            self.row_c = self.row_a
            self.column_c = self.column_b
        elif ((self.row_a == 1) and (self.row_b == 1) and (self.column_a == self.column_b)) and func == 3:
            result = 3  # разрешение для векторной алгебры проверка на то, что введеные матрицы вектора
        elif (self.column_a != self.column_b) and func == 4:
            result = 4  # вектора разной размерности
        elif (self.column_a == self.column_b) and (self.row_a == self.row_b) and func == 5:
            self.column_c = self.column_a
            result = 5

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
        self.c = choose_matrix(self.a, self.b)
        matrix = self.c
        # matrix = matrix_create(self.c.row, self.c.column)
        print('Enter the number:')
        n = float(input())
        for i in range(len(self.c)):
            for j in range(len(self.c[0])):
                matrix[i][j] = matrix[i][j] * n
        matrix_print(matrix)

    def transparent(self, a, b):
        if b == 0:
            self.a = a.matrix
        else:
            self.a = b
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
        return self.c

    def scalar_product(self):
        func = 3
        check_size = self.size_check(func)
        if check_size == 1:
            number = 0
            for i in range(len(self.a)):
                for j in range(len(self.a[i])):
                    number += self.a[i][j] * self.b[i][j]
            print("scalar product of A an B: %s" % number)
        elif self.column_a != 1:
            print("Matrix a is not a vector")
        elif self.column_b != 1:
            print("Matrix b is not a vector")
        elif check_size == 4:
            print("Different sizes of vectors")

    def len_vec(self):
        self.c = choose_matrix(self.a, self.b)
        matrix = self.c
        length = 0
        column = 0
        for i in range(1):
            for j in range(len(self.c[i])):  # проходим по одной строке, чтобы узнать размер
                column += 1  # количество столбцов в матрице
        if column == 1:
            for i in range(len(self.c)):
                for j in range(len(self.c[0])):
                    length += matrix[i][j] * matrix[i][j]
            length = math.sqrt(length)
            print('Length of chosen vector: %s' % length)
        else:
            print('Not vector!')
        return length

    def vec_mult(self):
        func = 5
        check_size = self.size_check(func)
        if check_size == 5:
            self.c = choose_matrix(self.a, self.b)
            for i in range(len(self.c)):
                for j in range(len(self.c[i])):
                    if i == len(self.c) - 1:
                        self.c[i][j] = ((self.a[0][j] * self.b[1][j]) - (self.a[1][j] * self.b[0][j]))
                    elif i == len(self.c) - 2:
                        self.c[i][j] = ((self.a[i + 1][j] * self.b[0][j]) - (self.a[0][j] * self.b[i + 1][j]))
                    elif i < len(self.c) - 2:
                        self.c[i][j] = ((self.a[i + 1][j] * self.b[i + 2][j]) - (self.a[i + 2][j] * self.b[i + 1][j]))
            matrix_print(self.c)
        elif self.row_a != 1:
            print("Matrix a is not a vector")
        elif self.row_b != 1:
            print("Matrix b is not a vector")
        else:
            print("No vectors detected!")

    def gaus(self, a, b):
        # разделяем на выбор
        # либо из приложения, либо из консоли
        # если запускается из консоли, необходимо указать параметр а равный 0
        # и наоборот (т.е. параметр b приравнять к нулю например, c.gaus(a, 0)
        if b == 0:
            self.c = a.matrix
        else:
            self.c = b
        n = 0
        for i in range(len(self.a)):  # количество строк в матрице
            n += 1  # размерность матрицы
        x = matrix_create(n, n)
        a = matrix_create(n, n)
        b = matrix_create(n, n)  # вспомогательная матрица, равная на каждом шаге предыдущей* матрице a
        sup = []
        sup2 = []
        sup3 = []
        sup4 = []
        for i in range(n):
            sup.append([])
            sup2.append([])
            sup3.append([])
            sup4.append([])
        for i in range(n):
            for j in range(n):
                a[i][j] = self.c[i][j]
        for i in range(n):
            for j in range(n):
                if i == j:
                    x[i][j] = 1
                else:
                    x[i][j] = 0
        # первый шаг из алгоритма, где делим на диагональный элемент
        for i in range(n):
            for j in range(n):
                if i != j:
                    if a[i][i] != 0:
                        a[i][j] = a[i][j] / a[i][i]
                        x[i][j] = x[i][j] / a[i][i]
                    elif a[i][i] == 0:
                        check = 0
                        d = i + 1
                        while check == 0:
                            check = a[d][d]
                            d += 1
                        if i < n:
                            for m in range(n):
                                sup2[m] = a[i][m]
                                sup[m] = a[d - 1][m]
                                sup4[m] = x[i][m]
                                sup3[m] = x[d - 1][m]
                            for m in range(n):
                                a[i][m] = sup[m]
                                a[d - 1][m] = sup2[m]
                                x[i][m] = sup3[m]
                                x[d - 1][m] = sup4[m]
                        if i == n:
                            for m in range(n):
                                sup2[m] = a[i][m]
                                sup[m] = a[0][m]
                                sup4[m] = x[i][m]
                                sup3[m] = x[0][m]
                            for m in range(n):
                                a[i][m] = sup[m]
                                a[d - 1][m] = sup2[m]
                                x[i][m] = sup3[m]
                                x[d - 1][m] = sup4[m]
                        a[i][j] = a[i][j] / a[i][i]
                        x[i][j] = x[i][j] / a[i][i]
                else:
                    x[i][j] = x[i][j] / a[i][i]
            for j in range(n):
                if i == j:
                    a[i][j] = 1
                else:
                    continue
            for m in range(n):
                for j in range(n):
                    b[m][j] = a[m][j]  # *прежде чем перейти к следующему шагу, необходимо запомнить предыдущий
            # второй шаг алгоритма (обнуляем элемент вне главной диагонали)
            for k in range(n):
                if k != i:
                    for j in range(n):
                        a[k][j] -= b[k][i] * b[i][j]
                        x[k][j] -= b[k][i] * x[i][j]
        print('Matrix x:')
        matrix_print(x)
        return x  # возвращаем обратную матрицу

    def holezkiy(self, a, b):
        if b == 0:
            self.c = a.matrix
            self.a = a.matrix
        else:
            self.c = b
        n = 0
        for i in range(len(self.c)):  # количество строк в матрице
            n += 1  # размерность матрицы
        flag = 0
        l = matrix_create(n, n)
        a = matrix_create(n, n)
        x = matrix_create(n, n)
        for i in range(1):
            if self.c[i][0] == 0:
                flag = 1
            else:
                flag = 0
        if self.c[n - 1][n - 1] == 0 or flag == 1:
            print("Impossible to use Holezkiy method")

        else:
            # self.c = matrix_create(n, n)
            # находим матрицу L
            for i in range(n):
                for j in range(n):
                    l[i][j] = 0
                    x[i][j] = 0
                    a[i][j] = self.c[i][j]
            l[0][0] = math.sqrt(a[0][0])
            for i in range(1, n):
                l[i][0] = a[i][0] / l[0][0]

            for j in range(1, n):
                summ = 0
                for p in range(j):
                    summ += math.pow(l[j][p], 2)
                l[j][j] = math.sqrt(a[j][j] - summ)
                for i in range(j + 1, n):
                    summ = 0
                    for p in range(i):
                        summ += l[j][p] * l[i][p]
                    l[i][j] = (a[i][j] - summ) / l[j][j]
            for i in range(n - 1, -1, -1):
                for j in range(i, -1, -1):
                    if i == j:
                        summ = 0
                        for k in range(i + 1, n):
                            summ += l[k][i] * x[k][i]
                        x[i][i] = (1 / l[i][i] - summ) / l[i][i]
                    else:
                        summ = 0
                        for k in range(j + 1, n):
                            summ += l[k][j] * x[k][i]
                        x[i][j] = - summ / l[j][j]
                        x[j][i] = x[i][j]

        matrix_print(l)
        print()
        matrix_print(x)
        return x
