def mirror_matrix(matrix):
    if (len(matrix) == 0) or (len(matrix[0]) == 0) or (len(matrix[0]) == 1):
        print(len(matrix))
    else:
        lenght = round(len(matrix[0]) / 2)
        for index, item in enumerate(matrix):
            if len(matrix[0]) % 2 == 0:
                end = -1
            else:
                end = -2
            matrix[index] = matrix[index][0:lenght]
            matrix[index] = matrix[index] + matrix[index][end::-1]
            