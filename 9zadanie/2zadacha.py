def findmaxel(matrix):
    n = len(matrix)
    maxel = float('-inf')
    maxelin = (0, 0)
    for i in range(n):
        if matrix[i][i] > maxel:
            maxel = matrix[i][i]
            maxelin = (i, i)
        if matrix[i][n-1-i] > maxel:
            maxel = matrix[i][n-1-i]
            maxelin = (i, n-1-i)
    ind = (n // 2, n // 2)
    matrix[maxelin[0]][maxelin[1]], matrix[ind[0]][ind[1]] = \
        matrix[ind[0]][ind[1]], matrix[maxelin[0]][maxelin[1]]
    return matrix
matrix = [
    [6, 3, 4],
    [1, 5, 9],
    [2, 8, 7]
]
res = findmaxel(matrix)
print("Вывод")
for row in res:
    print(row)
