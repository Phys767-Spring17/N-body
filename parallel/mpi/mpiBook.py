from mpi4py import MPI
from mpi4py.MPI import COMM_WORLD
from types import FunctionType

class Pool(object):
    """Process pool using MPI."""
    def __init__(self):
	self.f = None
	self.P = COMM_WORLD.Get_size()
	self.rank = COMM_WORLD.Get_rank()
    def wait(self):
	if self.rank == 0:
	    raise RuntimeError("Proc 0 cannot wait!")
	status = MPI.Status()
	while True:
	    task = COMM_WORLD.recv(source=0, tag=MPI.ANY_TAG, status=status)
	    if not task:
	    	break
	    if isinstance(task, FunctionType):
	    	self.f = task
	    	continue
	    result = self.f(task)
	    COMM_WORLD.isend(result, dest=0, tag=status.tag)

    def map(self, f, tasks):
	N = len(tasks)
	P = self.P
	Pless1 = P - 1
	if self.rank != 0:
	    self.wait()
	    return

	if f is not self.f:
	    self.f = f
	    requests = []
	    for p in range(1, self.P):
		r = COMM_WORLD.isend(f, dest=p)
		requests.append(r)
	    MPI.Request.waitall(requests)

	requests = []
	for i, task in enumerate(tasks):
	    r = COMM_WORLD.isend(task, dest=(i%Pless1)+1, tag=i)
	    requests.append(r)
	MPI.Request.waitall(requests)
	
	results = []
	for i in range(N):
	    result = COMM_WORLD.recv(source=(i%Pless1)+1, tag=i)
	    results.append(result)
	return results

    def __del__(self):
	if self.rank == 0:
	    for p in range(1, self.P):
		COMM_WORLD.isend(False, dest=p)

#def simulate(N, D, S, G, dt):
#    x0, v0, m = initial_cond(N, D)
#    pool = Pool()
#    if COMM_WORLD.Get_rank() == 0:
#	for s in range(S):
#	    x1, v1 = timestep(x0, v0, G, m, dt, pool)
#	    x0, v0 = x1, v1
#	else:
#	    pool.wait()

def simulate(N, D, S, G, dt):
    x0, v0, m = initial_cond(N, D)
    pool = Pool()
    if COMM_WORLD.Get_rank() == 0:
	for s in range(S):
	    with open("mpitest" + str(s) +".dat", "w") as myfile:
		x1, v1 = book.timestep(x0, v0, G, m, dt)
		x0, v0 = x1, v1
		for n in range(N):
		    myfile.write(str(x0[n,0]) + "  "
				+ str(x0[n,1]) + "  " + str(x0[n,2]) + "\n")
		myfile.flush()
    else:
	pool.wait()

if __name__ == '__main__':
    simulate(128, 3, 300, 1.0, 1e-3)
