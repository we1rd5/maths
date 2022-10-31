from create_matrix import create_matrix
import numpy
# Вычисление обратной матрицы, принимает одну матрицу


def inverse(a):
    a = numpy.array(matrix, dtype=numpy.float32)
    print("Обратная матрица:\n", numpy.linalg.inv(a))


if __name__ == "__main__":
    while True:
        matrix = create_matrix()
        inverse(matrix)
