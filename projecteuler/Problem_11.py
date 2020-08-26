matrix = \
    [
    [3, 8, 7, 9],
    [4, 1, 3, 2],
    [5, 6, 2, 9],
    [1, 2, 3, 4]
    ]

print(matrix)
matrix_slice = [[3, 8, 7, 9],
                [4, 1, 3, 2]]


def funky(matrix_slice):
    """
    :param matrix_slice: a slice of the matrix len = number of adjacent things (4)
    :return: product list.
    """

    x = lambda i: matrix_slice[0][i] * matrix_slice[1][i + 1]
    x_reverse = lambda o: matrix_slice[0][o] * matrix_slice[1][o - 1]
    product_list = []

    for b in range(0, 3):
        print(x(b))
        product_list.append(x(b))

    for c in range(3, 0, -1):
        print(x_reverse(c))
        product_list.append(x_reverse(c))

    return product_list

print(funky(matrix_slice))



# answer_4 = matrix_slice[0][3] * matrix_slice[1][4]
# maybe lambda?
