from create_matrix import create_matrix
import numpy
# Вычисление ранга, принимает одну матрицу


def find_rang(a):
    a = numpy.array(matrix, dtype=numpy.float32)
    r = numpy.linalg.matrix_rank(a)
    print("Матрица:\n", a)
    print("Ранг матрицы:", r)


if __name__ == "__main__":
    while True:
        matrix = create_matrix()
        find_rang(matrix)
