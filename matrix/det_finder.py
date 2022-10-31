from create_matrix import create_matrix
import numpy

def find_det(a):
    det = numpy.linalg.det(a)
    print("Матрица:\n", a)
    print("Определитель:\n", det)

if __name__ == "__main__":
    while True:
        matrix = create_matrix()
        a = numpy.array(matrix, dtype=numpy.float32)
        find_det(a)