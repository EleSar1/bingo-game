import sys
import os

sys.path.append(os.path.abspath(""))
from create_a_bingo_card.bingo_card import generate_bingo_card, display_bingo_card


def winning_card_check(bingo_card: dict) -> bool:

    """
    Checks if a Bingo card has a winning line.
    
    A winning line consists of five marked numbers (0) in a row, column, or diagonal.
    Returns True if the card has a winning line, otherwise returns False.

    Args: 
        bingo_card (dict): A dictionary representing the Bingo card, 
                           where keys are column labels ('B', 'I', 'N', 'G', 'O') 
                           and values are lists of numbers.

    Returns: 
        bool: True if card has a winning line, otherwise False.

    Raises:
        TypeError: If the parameter is not a dictionary.
    """

    if not isinstance(bingo_card, dict):
        raise TypeError("Expected dict, got a non-dict parameter.")
     
    bingo_label = list(bingo_card.keys())

    #check columns
    for letter in bingo_label:
        if all(bingo_card[letter][i] == 0 for i in range(5)):
            return True
    
    #check rows
    for i in range(5):
        if all(bingo_card[letter][i] == 0 for letter in bingo_label):
            return True

    #check main diagonal
    if all(bingo_card[bingo_label[i]][i] == 0 for i in range(5)):
        return True

    #check secondary diagonal
    if all(bingo_card[bingo_label[i]][4-i] == 0 for i in range(5)):
        return True

    return False
        

def main():

    #diagonal win
    winning_diagonal = generate_bingo_card()

    winning_diagonal["B"][0] = 0
    winning_diagonal["I"][1] = 0
    winning_diagonal["N"][2] = 0
    winning_diagonal["G"][3] = 0
    winning_diagonal["O"][4] = 0

    print(display_bingo_card(winning_diagonal))
    print(f"Winner? {winning_card_check(winning_diagonal)}\n")

    #columns win
    winning_col = generate_bingo_card()

    for i in range(5):
        winning_col["B"][i] = 0

    print(display_bingo_card(winning_col))
    print(f"Winner? {winning_card_check(winning_col)}\n")

    #rows win
    winning_rows = generate_bingo_card()

    for letter in "BINGO":
        winning_rows[letter][1] = 0
    
    print(display_bingo_card(winning_rows))
    print(f"Winner? {winning_card_check(winning_rows)}\n")

    #not win
    not_winner = generate_bingo_card()

    for i in range(4):
        not_winner["I"][i] = 0

    print(display_bingo_card(not_winner))
    print(f"Winner? {winning_card_check(not_winner)}\n")


if __name__ == "__main__":
    main()