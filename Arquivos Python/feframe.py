import numpy as np

def feframe2(el, xi, leng, area, rho, beta, ipt):
    a = el*area/leng
    c = el*xi/(leng**3)
    kl = np.array([
        [a, 0, 0, -a, 0, 0],
        [0, 12*c, 6*leng*c, 0, -12*c, 6*leng*c],
        [0, 6*leng*c, 4*leng**2*c, 0, -6*leng*c, 2*leng**2*c],
        [-a, 0, 0, a, 0, 0],
        [0, -12*c, -6*leng*c, 0, 12*c, -6*leng*c],
        [0, 6*leng*c, 2*leng**2*c, 0, -6*leng*c, 4*leng**2*c]
    ])
    r = np.array([
        [np.cos(beta), np.sin(beta), 0, 0, 0, 0],
        [-np.sin(beta), np.cos(beta), 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, np.cos(beta), np.sin(beta), 0],
        [0, 0, 0, -np.sin(beta), np.cos(beta), 0],
        [0, 0, 0, 0, 0, 1]
    ])
    k = r.T @ kl @ r
    m = None
    if ipt == 1:
        mm = rho*area*leng/420.0
        ma = rho*area*leng/6.0
        ml = np.array([
            [2*ma, 0, 0, ma, 0, 0],
            [0, 156*mm, 22*leng*mm, 0, 54*mm, -13*leng*mm],
            [0, 22*leng*mm, 4*leng**2*mm, 0, 13*leng*mm, -3*leng**2*mm],
            [ma, 0, 0, 2*ma, 0, 0],
            [0, 54*mm, 13*leng*mm, 0, 156*mm, -22*leng*mm],
            [0, -13*leng*mm, -3*leng**2*mm, 0, -22*leng*mm, 4*leng**2*mm]
        ])
        m = r.T @ ml @ r
    return k, m