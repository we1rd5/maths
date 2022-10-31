# Создание матрицы, запускать не нужно
def create_matrix():
    print("Введите матрицу согласно инструкции в readme.txt")
    n = ""
    matrix = []
    while n != "end":
        n = str(input())
        if n != "end":
            arr = n.split(' ')
            for i in arr:
                if i.isdigit():
                    i = int(i)
            matrix.append(arr)
    return matrix
