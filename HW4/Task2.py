# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(result)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[j][i] = matrix[i][j]

for i in matrix:
    print(i)
print()
for i in result:
    print(i)