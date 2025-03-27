import pytest 
import os
import sys

sys.path.append(os.path.abspath(""))
from play_bingo.play_bingo import simulate_n_games


def test_simulate_n_games():
    
    min_calls, max_calls, avg = simulate_n_games(1000)

    assert min_calls > 0, "Minimum calls should be more than 0."
    assert max_calls <= 75, "Maximum calls should be 75 or less."
    assert min_calls <= avg <= max_calls, "Average should be between min and max calls."

    assert isinstance(min_calls, int), "min_calls should be an integer."
    assert isinstance(max_calls, int), "max_calls should be an integer."
    assert isinstance(avg, float), "avg should be a floating point number."

    with pytest.raises(TypeError):
        simulate_n_games("1000")


if __name__ == "__main__":
    pytest.main()