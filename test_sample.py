from main import solve


def test_solve():
    assert solve([0, 1, 1, 1, 1, 1], 5) is True
    assert solve([1, 1, 1, 1, 1, 0], 0) is True
    assert solve([1, 2, 0, 1, 6, 7, 3, 3, 2, 1], 9) is True
    assert solve([1, 1, 1, 1, 1, 1], 0) is False
    assert solve([0, 9], 1) is False
