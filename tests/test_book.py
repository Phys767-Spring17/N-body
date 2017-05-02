import pytest


def test_book():
    from book.book import remove_i
    import numpy as np
    x = np.zeros((5, 3), dtype=float)
    y = remove_i(x, 2)
    assert np.size(x) == np.size(y) + 3
