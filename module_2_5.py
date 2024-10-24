def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_1 = []
        for j in range(m):
            list_1.append(value)

        matrix.append(list_1)

    print(matrix)


get_matrix(2,2,10)
get_matrix(3,5,42)
get_matrix(4,2,13)
