from multiprocessing import Pool
import numpy as np


def a(i, x, G, m):
        x_i = x[i]
        x_j = remove_i(x, i)
        m_j = remove_i(m, i)
        diff = x_j - x_i
        if np.any(diff) < 1:
                diff = 1
        else:
                mag3 = np.sum(diff**2, axis=1)**1.5
        result = G * np.sum(diff * (m_j / mag3)[:,np.newaxis], axis=0)
        return result

def timestep_i(args):
    """Computes the next position and velocity for the ith mass."""
    i, x0, v0, G, m, dt = args
    a_i0 = a(i, x0, G, m)
    v_i1 = a_i0 * dt + v0[i]
    x_i1 = a_i0 * dt**2 + v0[i] * dt + x0[i]
    return i, x_i1, v_i1

def timestep(x0, v0, G, m, dt, pool):
    """Computes the next position and velocity for all masses given
    initial conditions and a time step size.
    """
    N = len(x0)
    tasks = [(i, x0, v0, G, m, dt) for i in range(N)]
    results = pool.map(timestep_i, tasks)
    x1 = np.empty(x0.shape, dtype=float)
    v1 = np.empty(v0.shape, dtype=float)
    for i, x_i1, v_i1 in results:
	x1[i] = x_i1
	v1[i] = v_i1
    return x1, v1

