from create_matrix import create_matrix
import numpy

def inverse(a):
    print(numpy.linalg.inv(a))

if __name__ == "__main__":
    while True:
        matrix = create_matrix()
        a = numpy.array(matrix, dtype=numpy.float32)
        inverse(a)