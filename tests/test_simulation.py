import pytest


#def test_ic_7():
#    filename, N, D, S, G, dt = ic(7)
#    assert ic(7) == 'test', 1, 1, 1, 1, 1


def test_sim():
    from simulation.gravsim import simulate as sim
    assert sim(test, 1, 1, 1, 1, 1) == '\nSimulation complete. Your data has been saved as ' + sys.argv[1] + '*.dat\n'

