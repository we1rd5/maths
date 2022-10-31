from create_matrix import create_matrix
import numpy
# Вычисление определителя, принимает одну матрицу


def find_det(a):
    a = numpy.array(matrix, dtype=numpy.float32)
    det = numpy.linalg.det(a)
    print("Матрица:\n", a)
    print("Определитель:\n", det)


if __name__ == "__main__":
    while True:
        matrix = create_matrix()
        find_det(matrix)
