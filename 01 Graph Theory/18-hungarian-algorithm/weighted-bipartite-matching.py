def hungarian_algorithm(cost_matrix):
    def subtract_row_minima(matrix):
        for i in range(len(matrix)):
            row_min = min(matrix[i])
            for j in range(len(matrix[i])):
                matrix[i][j] -= row_min
        return matrix

    def subtract_column_minima(matrix):
        for j in range(len(matrix[0])):
            col_min = min(matrix[i][j] for i in range(len(matrix)))
            for i in range(len(matrix)):
                matrix[i][j] -= col_min
        return matrix

    def cover_zeros(matrix):
        zero_mask = [[matrix[i][j] == 0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        row_cover = [False] * len(matrix)
        col_cover = [False] * len(matrix[0])

        marked_zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if zero_mask[i][j] and not row_cover[i] and not col_cover[j]:
                    marked_zeros.append((i, j))
                    row_cover[i] = True
                    col_cover[j] = True

        row_cover = [False] * len(matrix)
        col_cover = [False] * len(matrix[0])
        for i, j in marked_zeros:
            row_cover[i] = True
            col_cover[j] = True

        return zero_mask, row_cover, col_cover, marked_zeros

    def step4(matrix, zero_mask, row_cover, col_cover):
        while True:
            uncovered_zeros = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if zero_mask[i][j] and not row_cover[i] and not col_cover[j]]
            if not uncovered_zeros:
                break
            i, j = uncovered_zeros[0]
            row_cover[i] = True
            col_cover[j] = False
        return col_cover

    def adjust_matrix(matrix, row_cover, col_cover):
        uncovered_elements = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if not row_cover[i] and not col_cover[j]]
        if not uncovered_elements:
            return matrix
        min_uncovered = min(uncovered_elements)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not row_cover[i] and not col_cover[j]:
                    matrix[i][j] -= min_uncovered
                if row_cover[i] and col_cover[j]:
                    matrix[i][j] += min_uncovered
        return matrix

    def find_optimal_assignment(cost_matrix, marked_zeros):
        row_ind = []
        col_ind = []
        assigned_rows = set()
        assigned_cols = set()

        for i, j in marked_zeros:
            if i not in assigned_rows and j not in assigned_cols:
                row_ind.append(i)
                col_ind.append(j)
                assigned_rows.add(i)
                assigned_cols.add(j)

        return row_ind, col_ind

    cost_matrix = [row[:] for row in cost_matrix]
    matrix = subtract_row_minima(cost_matrix)
    matrix = subtract_column_minima(matrix)

    while True:
        zero_mask, row_cover, col_cover, marked_zeros = cover_zeros(matrix)
        col_cover = step4(matrix, zero_mask, row_cover, col_cover)
        if sum(col_cover) >= len(matrix):
            break
        matrix = adjust_matrix(matrix, row_cover, col_cover)

    zero_mask, row_cover, col_cover, marked_zeros = cover_zeros(matrix)
    row_ind, col_ind = find_optimal_assignment(cost_matrix, marked_zeros)

    return row_ind, col_ind

# Example usage
cost_matrix = [
    [4, 2, 8],
    [2, 3, 7],
    [3, 1, 6]
]

row_ind, col_ind = hungarian_algorithm(cost_matrix)
print("Optimal assignment:")
for i, j in zip(row_ind, col_ind):
    print(f"Worker {i+1} assigned to job {j+1} with cost {cost_matrix[i][j]}")

total_cost = sum(cost_matrix[i][j] for i, j in zip(row_ind, col_ind))
print("Total cost:", total_cost)