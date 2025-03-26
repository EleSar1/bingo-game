import pytest
import sys
import os

sys.path.append(os.path.abspath(""))
from create_a_bingo_card.bingo_card import generate_bingo_card


def test_generate_bingo_card():

    card = generate_bingo_card()

    # Ensure the function returns a dictionary
    assert isinstance(card, dict), "Function should return a dictionary."

    # Ensure dictionary has the correct keys
    expected_keys = {"B", "I", "N", "G", "O"}
    assert set(card.keys()) == expected_keys, "Dictionary keys should be B, I, N, G, O."

    # Ensure each column contains exactly 5 numbers
    for key in expected_keys:
        assert len(card[key]) == 5, f"Column {key} must contain 5 numbers."
    
    # Ensure numbers in each column are unique
    for key in expected_keys:
        assert len(set(card[key])) == 5, f"Column {key} must contain unique numbers."

    # Ensure numbers fall within the correct range
    assert all(1 <= num <= 15 for num in card["B"]), "Numbers in 'B' must be between 1 and 15"
    assert all(16 <= num <= 30 for num in card["I"]), "Numbers in 'I' must be between 16 and 30"
    assert all(31 <= num <= 45 for num in card["N"]), "Numbers in 'N' must be between 31 and 45"
    assert all(46 <= num <= 60 for num in card["G"]), "Numbers in 'B' must be between 46 and 60"
    assert all(61 <= num <= 75 for num in card["O"]), "Numbers in 'O' must be between 61 and 75"


if __name__ == "__main__":

    pytest.main()