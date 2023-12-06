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

input_filename = "ДемиденковГеоргийДмитриевич_У-234_vvod.txt"
output_filename = "ДемиденковГеоргийДмитриевич_У-234_vivod.txt"

try:
    with open(input_filename, 'r') as file:
        lines = file.readlines()
        matrix = [[int(num) for num in line.split()] for line in lines]

    res = findmaxel(matrix)
    with open(output_filename, 'w') as output_file:
        for row in matrix:
            output_file.write(' '.join(map(str, row)) + '\n')

    print(f"Результаты были записаны в файл '{output_filename}'")
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print(f"Произошла ошибка: {e}")


