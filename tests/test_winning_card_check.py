import pytest
import os
import sys 

sys.path.append(os.path.abspath(""))
from checking_for_a_winning_card.winning_card import winning_card_check


def test_winning_card_check():

    winning_row = {
                    "B": [1, 0, 3, 4, 5],
                    "I": [16, 0, 18, 19, 20],
                    "N": [31, 0, 33, 34, 35],
                    "G": [46, 0, 48, 49, 50],
                    "O": [61, 0, 63, 64, 65]     
                }
    
    assert winning_card_check(winning_row) == True


if __name__ == "__main__":
    pytest.main()