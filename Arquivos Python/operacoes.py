import numpy as np
#Aplica as condições de contorno do problema na matriz
#de regidez e no vetor de forcas
def Cond_cont(K_mat, RAp, u_vec, DAp):
    n = len(u_vec)
    for i in range(n):
        c = u_vec[i] - 1
        K_mat[c, :] = 0
        K_mat[:, c] = 0
        K_mat[c, c] = 1
        RAp[c] = DAp[i]

    return K_mat, RAp

#Monta a matriz de rigidez global a partir juntando os elementos
def Matriz_K(K_mat, k_e, index):
    edof = len(index)
    for i in range(edof):
        ii = index[i]
        for j in range(edof):
            jj = index[j]
            K_mat[ii, jj] += k_e[i, j]
    return K_mat

#Calcula o indice dos deslocamentos u de um elemento
def u_vec_index(ind_el, num_nos_el, num_u_no):
    edof = num_nos_el*num_u_no
    start = (ind_el-1)*(num_nos_el-1)*num_u_no
    index = [start + i for i in range(edof)]
    
    u_ind = np.array(index, dtype=int)

    return u_ind

#Calcula a matriz global a partir da local e matriz de massa
def Matriz_Total_Global(E, I, L, area, phi, rho=1,Calc_massa=False):
    a1 = E*area/L
    a2 = E*I/(L**3)

    K_total = np.array([
        [a1, 0, 0, -a1, 0, 0],
        [0, 12*a2, 6*L*a2, 0, -12*a2, 6*L*a2],
        [0, 6*L*a2, 4*L**2*a2, 0, -6*L*a2, 2*L**2*a2],
        [-a1, 0, 0, a1, 0, 0],
        [0, -12*a2, -6*L*a2, 0, 12*a2, -6*L*a2],
        [0, 6*L*a2, 2*L**2*a2, 0, -6*L*a2, 4*L**2*a2]
    ])

    r = np.array([
        [np.cos(phi), np.sin(phi), 0, 0, 0, 0],
        [-np.sin(phi), np.cos(phi), 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, np.cos(phi), np.sin(phi), 0],
        [0, 0, 0, -np.sin(phi), np.cos(phi), 0],
        [0, 0, 0, 0, 0, 1]
    ])

    r_transp = r.T

    #matriz local K multiplica pela transposta de r 
    #para traduzir para a matriz global
    k = r_transp @ K_total @ r

    #Matriz de massa
    m = None

    if Calc_massa:
        mm = rho*area*L/420.0
        ma = rho*area*L/6.0
        ml = np.array([
            [2*ma, 0, 0, ma, 0, 0],
            [0, 156*mm, 22*L*mm, 0, 54*mm, -13*L*mm],
            [0, 22*L*mm, 4*L**2*mm, 0, 13*L*mm, -3*L**2*mm],
            [ma, 0, 0, 2*ma, 0, 0],
            [0, 54*mm, 13*L*mm, 0, 156*mm, -22*L*mm],
            [0, -13*L*mm, -3*L**2*mm, 0, -22*L*mm, 4*L**2*mm]
        ])
        m = r.T @ ml @ r
    return k, m
