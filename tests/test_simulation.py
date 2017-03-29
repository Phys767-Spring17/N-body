from simulation.gravsim import input_check as ic
import pytest


#def test_ic_7():
#     filename, N, D, S, G, dt = ic(7)
#    assert ic(7) == 'test', 1, 1, 1, 1, 1


def test_ic_not7():
    assert ic(1) == "SystemExit: 2"
