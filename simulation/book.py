import numpy as np
#""""""""""""""""""""""""""""""""""""""""
#
#""""""""""""""""""""""""""""""""""""""""
def remove_i(x, i):
	"""Drops the ith element of an array."""

	shape = (x.shape[0]-1,) + x.shape[1:]
	y = np.empty(shape, dtype=float)
	y[:i] = x[:i]
	y[i:] = x[i+1:]
	return y

#"""""""""""""""""""""""""""""""""""""""
#"""The acceleration of the ith mass."""
#"""""""""""""""""""""""""""""""""""""""
def a(i, x, G, m):
	x_i = x[i]
	x_j = remove_i(x, i)
	m_j = remove_i(m, i)
	diff = x_j - x_i
	mag3 = np.sum(diff**2, axis=1)**1.5
	result = G * np.sum(diff * (m_j / mag3)[:,np.newaxis], axis=0)
	return result

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#"""Computes the next position and velocity for all masses given""
#"""initial conditions and a time step size.""""""""""""""""""""""
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def timestep(x0, v0, G, m, dt):
	N = len(x0)
	x1 = np.empty(x0.shape, dtype=float)
	v1 = np.empty(v0.shape, dtype=float)
	for i in range(N):
		a_i0 = a(i, x0, G, m)
		v1[i] = a_i0 * dt + v0[i]
		x1[i] = a_i0 * dt**2 + v0[i] * dt + x0[i]
	return x1, v1
		
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#"""Generates initial conditions for N unity masses at rest""
#"""starting at random positions in D-dimensional space."""""
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def initial_cond(N, D):
	x0 = np.random.rand(N, D)-1000
	v0 = np.zeros((N, D), dtype=float)
	m = np.ones(N, dtype=float)
	return x0, v0, m
