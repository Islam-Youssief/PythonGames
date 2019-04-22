import simplegui
import random
import math

# variables used
end_range = 0
allowed_guesses = 0
computer_number = 0
user_number = 0


def range100():
    """Change the end range to be 100."""
    global end_range
    global allowed_guesses
    global computer_number

    end_range = 100
    allowed_guesses = math.ceil(math.log(end_range, 2))
    computer_number = random.randrange(0, end_range)

    print("New game. Range is from 0 to", end_range)
    print("Number of remaining guesses is", allowed_guesses, "\n")


def range1000():
    """Change the end range to be 1000."""
    global end_range
    global allowed_guesses
    global computer_number

    end_range = 1000
    allowed_guesses = math.ceil(math.log(end_range, 2))
    computer_number = random.randrange(0, end_range)

    print("New game. Range is from 0 to", end_range)
    print("Number of remaining guesses is", allowed_guesses, "\n")


def input_guess(guess):
    """Input user guess number."""
    global user_number
    global allowed_guesses

    try:
        user_number = int(guess)
    except ValueError:
        print("This,", guess, "is not a character !")
        return

    if user_number < 0 or user_number >= end_range:
        print("You have entered number that is out of range!\n")
        return

    allowed_guesses = allowed_guesses - 1

    print("Your Guess :", user_number)
    print("Number of remaining guesses is", allowed_guesses)

    if allowed_guesses > 0:
        # still has guess
        # get the right guess and restart the game.
        if computer_number == user_number:
            print('*' * 33, '\n', "~~~~ Woooooow you got it ! ~~~~", '\n', '*' * 33, '\n')
            if end_range == 100:
                range100()
            else:
                range1000()
        # computer guess is higher
        elif computer_number > user_number:
            print("Higher!", '\n')
        # computer guess is lower
        else:
            print("Lower!", '\n')
    else:
        # ran out of guess
        if computer_number == user_number:
            print('*' * 33, '\n', "~~~~ Woooooow you got it ! ~~~~", '\n', '*' * 33, '\n')
        else: print("You ran out of guesses. The Computer Guess was", computer_number, "\n")
        if end_range == 100:
            range100()
        else:
            range1000()


frame = simplegui.create_frame("~~ Guess the Number ~~", 250, 200)

# put the range buttons and input guess
frame.add_button("Change Range To (0, 100)", range100, 200)
frame.add_button("Change Range To (0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

range100()

# start the game
frame.start()
