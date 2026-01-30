from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # fencepole problem
    while front_is_clear():
        place_beeper_in_a_column()
        move_to_next_column()
    place_beeper_in_a_column()

def safe_put_beeper():
    if no_beepers_present():
        put_beeper()

def turn_around():
    turn_left()
    turn_left()

# pre: Karel is facing east on row 1
# post: Karel is facing east on row 1, after placing beepers
def place_beeper_in_a_column():
    turn_left()
    safe_put_beeper()
    while front_is_clear():
        move()
        safe_put_beeper()
    safe_put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_left()

# pre: Karel is facing east on row 1 of a column.
# post: Karel is facing east on row 1 of the next column.
def move_to_next_column():
    for i in range (4):
        move()
        

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
