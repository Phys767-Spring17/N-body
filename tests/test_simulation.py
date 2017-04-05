import pytest


#def test_ic_7():
#    filename, N, D, S, G, dt = ic(7)
#    assert ic(7) == 'test', 1, 1, 1, 1, 1


#def test_sim():
#    from simulation.gravsim import simulate as sim
#    assert sim(test, 1, 1, 1, 1, 1) == '\nSimulation complete. Your data has been saved as ' + sys.argv[1] + '*.dat\n'

def test_ic_7():
    from simulation.gravsim import input_check as ic
    with self.assertRaises(SystemExit) as cm:
        ic(5)

    self.assertEqual(cm.exception.code, 2)
