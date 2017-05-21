import numpy as np


def remove_i(x, i):
    """Drops the ith element of an array.
    
    """
    shape = (x.shape[0]-1,) + x.shape[1:]
    y = np.empty(shape, dtype=float)
    y[:i] = x[:i]
    y[i:] = x[i+1:]
    return y


def a(i, x, G, m):
    """The acceleration of the ith mass.
       This function also limits the value of diff to greater than 1.
    """
    x_i = x[i]
    x_j = remove_i(x, i)
    m_j = remove_i(m, i)
    diff = x_j - x_i
    if np.any(diff) < 1:
        diff = 1
    else:
        mag3 = np.sum(diff**2, axis=1)**1.5
    result = G * np.sum(diff * (m_j / mag3)[:, np.newaxis], axis=0)
    return result


def timestep(x0, v0, G, m, dt):
    """Computes the next position and velocity for all masses given
       initial conditions and a time step size.

    """
    N = len(x0)
    x1 = np.empty(x0.shape, dtype=float)
    v1 = np.empty(v0.shape, dtype=float)
    for i in range(N):
        a_i0 = a(i, x0, G, m)
        v1[i] = a_i0 * dt + v0[i]
        x1[i] = a_i0 * dt**2 + v0[i] * dt + x0[i]
    return x1, v1


def initial_cond(N, D):
    """Generates initial conditions for N unity masses at rest
       starting at random positions in D-dimensional space.

    """
    x0 = np.random.rand(N, D)-250
    for i in range(N/2):
        for j in range(D):
            x0[i, j] = x0[i, j]+500
    v0 = np.zeros((N, D), dtype=float)
    m = np.ones(N, dtype=float)
    return x0, v0, m
