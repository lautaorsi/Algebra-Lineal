import numpy as np
# Tests L04-LU


def calculaLU(A):
    print(A)
    cant_op = 0
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()
    
    if m!=n:
        print('Matriz no cuadrada')
        return
    
    ## desde aqui -- CODIGO A COMPLETAR

    for i in range(m):
        if np.linalg.det(A) == 0:            ##TODO: CALCULAR DETERMINANTE DE SUS SUBMATRICES PRINCIPALES
            return None, None, None


    L = np.zeros((m,n))
    

    for i in range(m):
        L[i][i] = 1

        
    U = A.copy()

    for i in range(m):
        for j in range(i+1,m):
            if U[j][i] != 0: 
                cant_op += 1 + (2* (m - (i+1)))
                if U[i][i] == 0:
                    return None, None, None
                Mi = (U[j][i] / U[i][i])
                U[j] = U[j] -  ( Mi * U[i])
                L[j][i] = Mi
                
    ## hasta aqui, calculando L, U y la cantidad de operaciones sobre 
    ## la matriz Ac
            
    print(L)
    print(U)
    print(cant_op)
    return L, U, cant_op

def res_tri(L,b,inferior=True):
    print("asd")
    filasL = L.shape[0]
    res = np.zeros(filasL)
    if inferior:
        for i in range(filasL):
            res[i] = b[i]
            for j in range(i):
                res[i] -= L[j] * res[j] 
    else:

        for i in range(filasL, 0):
            
            res[i] = b[i]
            for j in range(i):
                res[i] -= L[j] * res[j]     


def main():

    # Tests LU
    
    L0 = np.array([[1,0,0],[0,1,0],[1,1,1]])
    U0 = np.array([[10,1,0],[0,2,1],[0,0,1]])
    A =  L0 @ U0
    L,U,nops = calculaLU(A)
    assert(np.allclose(L,L0))
    assert(np.allclose(U,U0))
    
    
    L0 = np.array([[1,0,0],[1,1.001,0],[1,1,1]])
    U0 = np.array([[1,1,1],[0,1,1],[0,0,1]])
    A =  L0 @ U0
    
    L,U,nops = calculaLU(A)
    assert(not np.allclose(L,L0))
    assert(not np.allclose(U,U0))
    assert(np.allclose(L,L0,atol=1e-3))
    assert(np.allclose(U,U0,atol=1e-3))
    assert(nops == 13)
    
    L0 = np.array([[1,0,0],[1,1,0],[1,1,1]])
    U0 = np.array([[1,1,1],[0,0,1],[0,0,1]])
    A =  L0 @ U0
    L,U,nops = calculaLU(A)
    assert(L is None)
    assert(U is None)
    assert(nops == 0)

    ## Tests res_tri

    A = np.array([[1,0,0],[1,1,0],[1,1,1]])
    b = np.array([1,1,1])
    assert(np.allclose(res_tri(A,b),np.array([1,0,0])))
    b = np.array([0,1,0])
    assert(np.allclose(res_tri(A,b),np.array([0,1,-1])))
    b = np.array([-1,1,-1])
    assert(np.allclose(res_tri(A,b),np.array([-1,2,-2])))
    b = np.array([-1,1,-1])
    assert(np.allclose(res_tri(A,b,inferior=False),np.array([-1,1,-1])))

    A = np.array([[3,2,1],[0,2,1],[0,0,1]])
    b = np.array([3,2,1])
    assert(np.allclose(res_tri(A,b,inferior=False),np.array([1/3,1/2,1])))

    A = np.array([[1,-1,1],[0,1,-1],[0,0,1]])
    b = np.array([1,0,1])
    assert(np.allclose(res_tri(A,b,inferior=False),np.array([1,1,1])))


if __name__ == "__main__":
    main()
    
    

# # Test inversa

# ntest = 10
# iter = 0
# while iter < ntest:
#     A = np.random.random((4,4))
#     A_ = inversa(A)
#     if not A_ is None:
#         assert(np.allclose(np.linalg.inv(A),A_))
#         iter += 1

# # Matriz singular devería devolver None
# A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# assert(inversa(A) is None)




# # Test LDV:

# L0 = np.array([[1,0,0],[1,1.,0],[1,1,1]])
# D0 = np.diag([1,2,3])
# V0 = np.array([[1,1,1],[0,1,1],[0,0,1]])
# A =  L0 @ D0  @ V0
# L,D,V,nops = calculaLDV(A)
# assert(np.allclose(L,L0))
# assert(np.allclose(D,D0))
# assert(np.allclose(V,V0))

# L0 = np.array([[1,0,0],[1,1.001,0],[1,1,1]])
# D0 = np.diag([3,2,1])
# V0 = np.array([[1,1,1],[0,1,1],[0,0,1.001]])
# A =  L0 @ D0  @ V0
# L,D,V,nops = calculaLDV(A)
# assert(np.allclose(L,L0,1e-3))
# assert(np.allclose(D,D0,1e-3))
# assert(np.allclose(V,V0,1e-3))

# # Tests SDP

# L0 = np.array([[1,0,0],[1,1,0],[1,1,1]])
# D0 = np.diag([1,1,1])
# A = L0 @ D0 @ L0.T
# assert(esSDP(A))

# D0 = np.diag([1,-1,1])
# A = L0 @ D0 @ L0.T
# assert(not esSDP(A))

# D0 = np.diag([1,1,1e-16])
# A = L0 @ D0 @ L0.T
# assert(not esSDP(A))

# L0 = np.array([[1,0,0],[1,1,0],[1,1,1]])
# D0 = np.diag([1,1,1])
# V0 = np.array([[1,0,0],[1,1,0],[1,1+1e-10,1]]).T
# A = L0 @ D0 @ V0
# assert(not esSDP(A))