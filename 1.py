class Matrix:
    def __init__(self, list_1, list_2):

        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0], [0, 0], [0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]) #почему не работает если тут return матрицу, смысл тогда от def __str__

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]])

print(my_matrix.__add__())