import pytest
import os
import sys
from tabulate import tabulate

sys.path.append(os.path.abspath(""))
from create_a_bingo_card.bingo_card import display_bingo_card


def test_display_bingo_card():

    #sample valid bingo card
    bingo_card = {
                    "B": [1, 2, 3, 4, 5],
                    "I": [16, 17, 18, 19, 20],
                    "N": [31, 32, 33, 34, 35],
                    "G": [46, 47, 48, 49, 50],
                    "O": [61, 62, 63, 64, 65]
                }

    #The function should return a string
    result = display_bingo_card(bingo_card)
    assert isinstance(result, str), "The function should return a string."

    #The output should contain the column headers
    for header in ["B", "I", "N", "G", "O"]:
        assert header in result, f"Output should contain column '{header}'."

    #The function should use tabulate and have a grid format
    expected_output = tabulate(bingo_card, headers="keys", tablefmt="grid")
    assert result == expected_output, "The formatted output does not match expected tabulated structure."

    #The function should raise TypeError for invalid input
    with pytest.raises(TypeError):
        display_bingo_card("not a dictionary") 


if __name__ == "__main__":
    pytest.main()