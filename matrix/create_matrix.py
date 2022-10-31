def create_matrix():
    n = ""
    matrix = []
    while n != "end":
        n = str(input())
        if n != "end":
            arr = n.split(' ')
            for i in arr:
                i = int(i)
            matrix.append(arr)
    return matrix