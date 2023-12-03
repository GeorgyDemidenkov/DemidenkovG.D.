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

def readfile(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
    return matrix

def writefile(file_name, maxelrow, minelcolumn):
    with open(file_name, 'w') as file:
        file.write(f"Наибольшие элементы в строках: {maxelrow}\n")
        file.write(f"Наименьшие элементы в столбцах: {minelcolumn}\n")

input_file_name = "ДемиденковГеоргийДмитриевич_У-234_vvod.txt"
output_file_name = "ДемиденковГеоргийДмитриевич_У-234_vivod.txt"

A = readfile(input_file_name)
maxelrow, minelcolumn = find(A)
writefile(output_file_name, maxelrow, minelcolumn)
