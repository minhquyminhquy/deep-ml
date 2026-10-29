def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    num_cols_a = len(a[0])
    num_rows_b = len(b)
    num_cols_b = len(b[0])
    if num_cols_a != num_rows_b:
        return -1

    matrix_c = []

    for row_a in a:
        row_c = []
        for col_b_idx in range(num_cols_b):
            row_ele_c = 0
            col_b = [row_b[col_b_idx] for row_b in b]
            for row_ele_a, col_ele_b in zip(row_a, col_b):
                row_ele_c += row_ele_a * col_ele_b
            row_c.append(row_ele_c)
        matrix_c.append(row_c)
    return matrix_c
            