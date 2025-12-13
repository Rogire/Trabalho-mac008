import numpy as np

def feeldof1(iel, nnel, ndof):
    edof = nnel*ndof
    start = (iel-1)*(nnel-1)*ndof
    index = [start + i for i in range(edof)]
    return np.array(index, dtype=int)