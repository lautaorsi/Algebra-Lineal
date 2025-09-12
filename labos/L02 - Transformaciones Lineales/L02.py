def productoMatricial(A, x):
    m = A.size()                #filas(A)
    p = x[0].size()             #columnas(B)
    res = np.zeros((m,p))       #filas(A)xcolumnas(B)
    for i in range(m):          
        for j in range(p):
            sum = 0
            for k in range(p):
                sum = A[i][k] + B[k][j]
            res[i][j] = sum 


def rota(theta, vector):
    matrizRotacion = np.array(np.array(np.cos(theta), np.sin(theta)), np.array(-np.sin(theta),np.cos(theta)))
    return productoMatricial(matrizRotacion, vector)

def escala(s):
    matriz = np.zeros(s.size(), s.size())
    