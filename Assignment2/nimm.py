"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    num_stone_left = 20
    tPlayers = ("Player 1", "Player 2")
    current_player = tPlayers[0]

    while num_stone_left > 0: 
        print(f'There are {num_stone_left} left.')
        num_stone_removed = int(input(f'{current_player}, would you like to remove 1 or 2 stones? '))
        # check if user enters a valid number.
        # if the number is invalid, keep asking user to enter a valid number (1 or 2)
        while num_stone_removed != 1 and num_stone_removed != 2:
            num_stone_removed = int(input(f'Please enter 1 or 2: '))
        num_stone_left -= num_stone_removed
        # Fencepole problem
        # get next player returns next player
        current_player = get_next_player(tPlayers, current_player)
    current_player = get_next_player(tPlayers, current_player)
    
    print("game over")
    print(f'{current_player}, you lost!')

def get_next_player(tP, p):
        if p == tP[0]:
             return tP[1]
        else:
            return tP[0]


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
