import random

def number_to_name(number):
    """ Returns name realted to specific number using dictionary."""

    game_dict = {0: "rock",
                 1: "Spock",
                 2: "paper",
                 3: "lizard",
                 4: "scissors"}
    return game_dict.get(number, "The number is out of range!")


def name_to_number(name):
    """ Returns number realted to specific name using dictionary."""

    game_dict = {"rock": 0,
                 "Spock": 1,
                 "paper": 2,
                 "lizard": 3,
                 "scissors": 4}
    return game_dict.get(name, "Invalid name!")


def rpsls(name):
    """ Starting point in the game."""
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5

    # use if/elif/else to determine winner
    if difference == 0:
        result = "Player and computer tie!"
    elif difference == 1 or difference == 2:
        result = "Player wins!"
    else:
        result = "Computer wins!"

    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)

    # print results
    print "Player chooses", name
    print "Computer chooses", comp_name
    print result,'\n'
    if name != "scissors":
        print
        
# test my code
rpsls("lizard")
rpsls("scissors")
rpsls("rock")
rpsls("Spock")
rpsls("paper")
