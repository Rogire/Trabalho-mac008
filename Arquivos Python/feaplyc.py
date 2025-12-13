def feaplyc2(kk, ff, bcdof, bcval):
    n = len(bcdof)
    for i in range(n):
        c = bcdof[i] - 1
        kk[c, :] = 0
        kk[:, c] = 0
        kk[c, c] = 1
        ff[c] = bcval[i]
    return kk, ff