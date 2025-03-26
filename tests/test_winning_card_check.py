import pytest
import os
import sys 

sys.path.append(os.path.abspath(""))
from checking_for_a_winning_card.winning_card import winning_card_check


def test_winning_row():

    winning_row = {
                    "B": [1, 0, 3, 4, 5],
                    "I": [16, 0, 18, 19, 20],
                    "N": [31, 0, 33, 34, 35],
                    "G": [46, 0, 48, 49, 50],
                    "O": [61, 0, 63, 64, 65]     
                }
    
    assert winning_card_check(winning_row) == True, f"Result for {winning_row} must be True"


def test_winning_col():

    winning_col = {
                    "B": [0, 0, 0, 0, 0],
                    "I": [16, 17, 18, 19, 20],
                    "N": [31, 32, 33, 34, 35],
                    "G": [46, 47, 48, 49, 50],
                    "O": [61, 62, 63, 64, 65]     
                }
    
    assert winning_card_check(winning_col) == True, f"Result for {winning_col} must be True"


def test_winning_diagonals():

    winning_primary = {
                    "B": [0, 2, 3, 4, 5],
                    "I": [16, 0, 18, 19, 20],
                    "N": [31, 32, 0, 34, 35],
                    "G": [46, 47, 48, 0, 50],
                    "O": [61, 62, 63, 64, 0]     
                }
    
    assert winning_card_check(winning_primary) == True, f"Result for {winning_primary} must be True"

    winning_secondary = {
                    "B": [1, 2, 3, 4, 0],
                    "I": [16, 17, 18, 0, 20],
                    "N": [31, 32, 0, 34, 35],
                    "G": [46, 0, 48, 49, 50],
                    "O": [0, 62, 63, 64, 65]     
                }
    
    assert winning_card_check(winning_secondary) == True, f"Result for {winning_secondary} must be True"


def test_not_winner():

    not_winner = {
                    "B": [1, 2, 3, 4, 5],
                    "I": [16, 0, 18, 19, 20],
                    "N": [31, 32, 0, 34, 35],
                    "G": [46, 47, 48, 0, 50],
                    "O": [61, 62, 63, 64, 0]     
                }
    
    assert winning_card_check(not_winner) == False, f"Result for {not_winner} must be False"


def test_raise_errors():

    with pytest.raises(TypeError):

        winning_card_check(15)


if __name__ == "__main__":
    pytest.main()