"""
File: sentinelloop.py
------------------
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

def main():
    total = 0
    guess = 0

    # FKUNG - fence problem !
    # needs to place the statement before the 
    # while loop and not enter the loop for -1
    # ask for number - post
    # add number to total - fence
    guess = int(input("enter a number: "))
    while (guess != -1):
        total += guess
        guess = int(input("enter a number: "))

    print(f'total is: {total}')

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()