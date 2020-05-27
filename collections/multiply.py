def multiply(matrix_A, matrix_B):
    result = []
    n = len(matrix_B[0]) - 1
    for index_A, item_A in enumerate(matrix_A):
        count_B = 0
        temp_result = []
        while count_B <= n:
            iter_matrix_B = iter(matrix_B)
            row_element = 0
            for item in item_A:
                row_element += item * next(iter_matrix_B)[count_B]
            temp_result.append(row_element)
            count_B += 1
        result.extend([temp_result])
    return result
