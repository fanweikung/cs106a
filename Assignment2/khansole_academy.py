"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    COUNT_TO_WIN = 3
    correct_count = 0
    # get 2 random numbers between 10 and 99
    while correct_count < COUNT_TO_WIN:
        int1 = random.randint(10, 99)
        int2 = random.randint(10, 99)
        correct_answer = int1 + int2
        # prompt to get the addition of the two numbers
        print(f'number 1: {int1}')
        print(f'number 2: {int2}')
        user_answer = int(input(f'The addition of the two numbers is: '))
        # if the answer is correct 3 times in a row, the user wins.
        # if not, continue
        if user_answer == correct_answer:
            correct_count += 1
            print(f'Correct! You have answered correctly {correct_count} in a row. {COUNT_TO_WIN - correct_count} more to win!')
            if (correct_count == COUNT_TO_WIN):
                print('***\nCongratulation! You have won!! 👏👏👏\n***')
        else:
            correct_count = 0
            print(f'Incorrect. {COUNT_TO_WIN} correct answers in a row to win.😭😭😭')
            print(f'The correct answer is {correct_answer}. Nice try.\n\nStart over... ^o^ ')



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
