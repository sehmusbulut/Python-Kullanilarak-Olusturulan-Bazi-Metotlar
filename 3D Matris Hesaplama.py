    #3D Matris Hesaplama
def matrix_3d(m, n, p):
    # m, n, p: matrisin boyutları (m x n x p)
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append([])
            for k in range(p):
                # Burada, her bir eleman için bir değer atayabilirsiniz
                # Örneğin, her elemanı 0 olarak ayarlayabilirsiniz:
                matrix[i][j].append(0)
    return matrix
