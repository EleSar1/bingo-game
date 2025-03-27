import pytest
import os
import sys

sys.path.append(os.path.abspath(""))
from play_bingo.play_bingo import play_bingo


def test_play_bingo():

    calls = play_bingo()

    assert isinstance(calls, int), "Number of calls must be an integer."

    # The theoretical minimum calls to win is 5 (a complete column immediately)
    assert calls >= 5, "The number of calls must be at least 5."
    # The maximum number of calls should be 75 (last possible draw)
    assert calls <= 75, "The number of calls cannot exceed 75."


if __name__ == "__main__":
    pytest.main()