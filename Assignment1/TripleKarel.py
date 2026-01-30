from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # pre: Karel is facing west at the north east corner
    # post: Karel painted 3 sides and stand in between the 3rd and 4th side (unpainted).
    def paint_a_building():
        for i in range(3):
            paint_one_side()
            turn_left()
            move()
            paint_one_side()
            turn_left()
            move()
            paint_one_side()
            if front_is_blocked():
                turn_right()


    def paint_one_side():
        while left_is_blocked():
            put_beeper()
            move()
    
    def turn_right():
        turn_left()
        turn_left()
        turn_left()
    
    paint_a_building()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
