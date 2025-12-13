import numpy as np

def feasmbl1(kk, k, index):
    edof = len(index)
    for i in range(edof):
        ii = index[i]
        for j in range(edof):
            jj = index[j]
            kk[ii, jj] += k[i, j]
    return kk