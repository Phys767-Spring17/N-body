import pytest


def test_ic_7():
    from simulation.gravsim import input_check as ic
    import sys
    sys.argv = ["gravsim.py", "test", 1, 3, 1, 1, 1]
    filename, N, D, S, G, dt = ic(7)
    assert filename == "test"

def test_sim():
    from simulation.gravsim import input_check as ic
    import sys
    sys.argv = ["gravsim.py", "test", 1, 3, 1, 1, 1]
    filename, N, D, S, G, dt = ic(7)
    assert N == 1, D == 3
