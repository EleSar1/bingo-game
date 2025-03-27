import pytest
import os
import sys

sys.path.append(os.path.abspath(""))
from play_bingo.play_bingo import shuffle_bingo_numbers


def test_shuffe_bingo_numbers():

    numbers = shuffle_bingo_numbers()

    assert isinstance(numbers, list), "Result should be a list."
    assert len(numbers) == 75, "List should contain exactly 75 numbers."

    letters = set(num[0] for num in numbers)
    assert letters == {"B", "I", "N", "G", "O"}, "List should countains only B, I, N, G, O letters."

    columns = {
                "B": range(1,16),
                "I": range(16,31),
                "N": range(31,46),
                "G": range(46,61),
                "O": range(61,76)
                }

    for num in numbers: 
        letter, number = num[0], int(num[1:])
        assert number in columns[letter]


def test_shuffle_bingo_numbers_randomness():

    numbers1 = shuffle_bingo_numbers()
    numbers2 = shuffle_bingo_numbers()

    assert numbers1 != numbers2


if __name__ == "__main__":
    pytest.main()
