import numpy as np

def esCuadrada(matriz):
    for fila in matriz:
        if fila.size != len(matriz):    ## Si la cantidad de elementos en la fila es distinta a la cantidad de filas 
            return False                ## entonces no es cuadrada
    return True



def triangSup(matriz):
    if  not(esCuadrada(matriz)):        ## Para calcular la matriz triangular necesito que sea cuadrada
        return "La matriz no es cuadrada"
    
    for i in range(len(matriz) - 1):    ## Hago gauss con mcm para cada posicion 
        matriz[i+1] = (matriz[i+1] * matriz[i][i])  - (matriz[i] * matriz[i+1][i])
    for i in range(len(matriz)):        ## Nos piden que no tenga la diagonal, seteo en 0
        matriz[i][i] = 0
                                        ## Modifique la matriz pasada x parametro, no aclara si necesita preservar el param

def triangInf(matriz):
    if not(esCuadrada(matriz)):         ## Para calcular la matriz triangular necesito que sea cuadrada
        return "La matriz no es cuadrada"
    
    for i in range(len(matriz) - 1):    ## Hago gauss con mcm para cada posicion 
        matriz[i+1] = (matriz[i+1] * matriz[i][i])  - (matriz[i] * matriz[i+1][i])
    for i in range(len(matriz)):        ## Nos piden que no tenga la diagonal, seteo en 0
        matriz[i][i] = 0

def diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(matriz[i].size):
            if i != j:
                matriz[i][j] = 0

def main():
    a_matrix = np.array([[5,3,2],[10,8,1],[10,25,3]])
    triangSup(a_matrix)
    print(a_matrix)
    return 0


if __name__ == '__main__':
    main()