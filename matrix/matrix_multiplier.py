from create_matrix import create_matrix
import numpy

def multiply_matrix(a, b):
    a = numpy.array(a, dtype=numpy.float32)
    b = numpy.array(b, dtype=numpy.float32)
    print(a.dot(b))

if __name__ == "__main__":
    n = ""
    while True:
        matrix_a = create_matrix()
        matrix_b = create_matrix()
        multiply_matrix(matrix_a, matrix_b)