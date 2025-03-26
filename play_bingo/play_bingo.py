from random import shuffle
import os
import sys

sys.path.append(os.path.abspath(""))
from create_a_bingo_card.bingo_card import generate_bingo_card
from checking_for_a_winning_card.winning_card import winning_card_check


def shuffle_bingo_numbers() -> list:

    """
    Generates a list of Bingo numbers, assigns them to their respective columns (B, I, N, G, O),
    shuffles them randomly, and returns the shuffled list.

    Returns:
        list: A shuffled list of Bingo numbers in the format 'LetterNumber' (e.g., 'B12', 'G55').
    """

    bingo_numbers = []
    columns = {
                "B": range(1,16),
                "I": range(16,31),
                "N": range(31,46),
                "G": range(46,61),
                "O": range(61,76)
                }

    for letter, numbers in columns.items():
        bingo_numbers.extend([f"{letter}{num}" for num in numbers])

    shuffle(bingo_numbers)

    return bingo_numbers


def play_bingo():

    """
    Simulates a single game of Bingo.

    A Bingo card is generated, and numbers are drawn one by one from a shuffled list.
    If a drawn number is present on the card, it is marked (set to 0).
    The game continues until the card has a winning line (row, column, or diagonal).

    Returns:
        int: The number of calls required to achieve a Bingo.
    """

    bingo_card = generate_bingo_card()
    bingo_numbers = shuffle_bingo_numbers()
    count_calls = 0

    for extracted in bingo_numbers:
        count_calls += 1
        num = int(extracted[1:])
        column = extracted[0]

        for i in range(5):    
            if bingo_card[column][i] == num:
                bingo_card[column][i] = 0

        if winning_card_check(bingo_card):
            return count_calls     


def simulate_n_games(n=1000):

    """
    Simulates multiple games of Bingo and collects statistics on the number of calls needed to win.

    Args:
        n (int, optional): The number of Bingo games to simulate. Defaults to 1000.

    Returns:
        tuple: A tuple containing:
            - min_calls (int): The minimum number of calls needed to win a game.
            - max_calls (int): The maximum number of calls needed to win a game.
            - avg (float): The average number of calls needed to win a game.
    """

    count_calls = [play_bingo() for _ in range(n)]
    
    min_calls = min(count_calls)
    max_calls = max(count_calls)
    avg = sum(count_calls) / len(count_calls)

    return min_calls, max_calls, avg


def main():
    
    min_calls, max_calls, avg = simulate_n_games()

    print("Results after 1000 games:")
    print(f"Minimum number of calls to win: {min_calls}")
    print(f"Maximum number of calls to win: {max_calls}")
    print(f"Average number of calls to win: {avg:.2f}")


if __name__ == "__main__":
    main()


