import classes


# создаем матрицу сначала строки, потом столбцы
# если вектор, то cтрока = 1
# a = classes.Tmatrix(1, 2)
# b = classes.Tmatrix(1, 2)
# c = classes.lin_alg(a, b)
# c.sum()
# c.mult()
# c.mult_mat_number()
# c.transparent()
# c.scalar_product()


def get_information():
    print('To enter new matrix - [0] '
          'or [ENTER NEW MATRIX]')
    print('[CREATE] matrix C as the result of some functions between matrix A and B - [1]')
    print('[SUM] or [2] t find sum of matrix A and matrix B')
    print('[MULT] or [3] to find product of multivariance A and B')
    print(' If you want to find the length of vector type [LEN] of [4]')


def error():
    print('Matrix C not initialized')
    print('use command [CREATE] or [2] to initialize it')


def main():
    matrix = []
    print('Welcome to linear algebra application')
    print('Here you can use some basic functions')
    print('Call function [HELP] if you want to see them')
    print('Type [EXIT] if you wanna leave application')
    cycling = 1
    i = 0  # количество матриц введеных пользователем
    flag = 0  # указатель на то, что матрица C была создаа
    while cycling == 1:
        print('Type command right here:')
        choice = input().upper()
        if choice == 'HELP':
            get_information()
            continue
        if choice == '0' or choice == 'ENTER NEW MATRIX' or choice == 'NEW':
            print('Enter rows and columns:')
            print('Columns first rows after')
            column = int(input())
            row = int(input())
            matrix.append([])
            matrix[i] = classes.Tmatrix(row, column)
            i += 1
            continue
        if choice == 'CREATE' or choice == '1':
            if i >= 2:
                print('Now you have %s matrix' % i)
                print('Enter A = index of matrix[i] and B')
                index_1 = int(input())
                index_2 = int(input())
                c = classes.lin_alg(matrix[index_1], matrix[index_2])
                flag = 1
                continue
            else:
                print('One matrix is not enough')
                print('Enter new matrix by using command [NEW] or type [0]')
                flag = 0
                continue
        if choice == 'CHEAT':
            c = classes.lin_alg(matrix[0], matrix[1])
            flag = 1
            continue
        if choice == 'SUM' or choice == '2':
            if flag == 1:
                c.sum()
                continue
            else:
                error()
                continue
        if choice == 'MULT' or choice == '3':
            if flag == 1:
                c.mult()
                continue
            else:
                error()
        if choice == 'LEN' or choice == '4':
            if flag == 1:
                c.len_vec()
                continue
            else:
                error()
        if choice == '5' or choice =='TRANSPARENT':
            if flag == 1:
                a = classes.choose_matrix(matrix[0], matrix[1])
                c.transparent(a, 0)
                continue
            else:
                error()
        if choice == 'MULTNUM' or choice == '6':
            if flag == 1:
                c.mult_mat_number()
                continue
            else:
                error()
        if choice == 'SCALAR' or choice == '7':
            if flag == 1:
                c.scalar_product()
                continue
            else:
                error()
        if choice == '8' or choice == 'VECMULT':
            if flag == 1:
                c.vec_mult()
                continue
            else:
                error()
        if choice == '9' or choice == 'GAUS':
            if flag == 1:
                a = classes.choose_matrix(matrix[0], matrix[1])
                c.gaus(a, 0)
                continue
            else:
                error()
        if choice == '10' or choice == 'HOLEZKIY':
            if flag == 1:
                a = classes.choose_matrix(matrix[0], matrix[1])
                c.holezkiy(a, 0)
                continue
            else:
                error()
        if choice == 'EXIT':
            print('C`ao')
            cycling = 0
        else:
            print('Unknown command, try again')


main()
