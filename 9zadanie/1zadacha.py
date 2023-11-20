def find(matrix):
    maxelrow = []
    minelcolumn = []
    for row in matrix:
        maxel = max(row)
        maxelrow.append(maxel)
    transposed_matrix = list(zip(*matrix))
    for column in transposed_matrix:
        minel = min(column)
        minelcolumn.append(minel)
    return maxelrow, minelcolumn
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
maxelrow, minelcolumn = find(matrix)
print("Наибольшие элементы в строках:", maxelrow)
print("Наименьшие элементы в столбцах:", minelcolumn)
