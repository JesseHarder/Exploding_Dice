"""
Exploding Dice

Written by Jesse Harder, Copyright 2017

This program contains code for m odeling success probabilities for rolling exploding dice in ways akin to that of the
Burning Wheel test system.
"""

from random import *


DEFAULT_DIE_SIZE = 6
DEFAULT_SUCCESS_THRESHOLD = 4


# Function: roll_exploding_die
# Parameters:
#   num_sides - expected to be an integer > 0.
#       Default value is DEFAULT_DIE_SIZE
#   num_sides - expected to be an integer > 0.
#       Default value is DEFAULT_SUCCESS_THRESHOLD
# Return Value: The number of successes obtained from a simulation of rolling an exploding die with num_sides sides and
#               when a success is any roll of success_threshold or higher.
def roll_exploding_die(num_sides=DEFAULT_DIE_SIZE, success_threshold=DEFAULT_SUCCESS_THRESHOLD):
    assert num_sides > 0

    successes = 0;

    # First roll.
    roll = randint(1, num_sides)
    if roll >= success_threshold:
        successes += 1;

    # Exploding rerolls.
    while roll == num_sides:
        roll = randint(1, num_sides)
        if roll >= success_threshold:
            successes += 1;

    return successes


# Function: roll_exploding_dice
# Parameters:
#   num_dice- expected to be an integer > 0.
#       Default value is 1
#   num_sides - expected to be an integer > 0.
#       Default value is DEFAULT_DIE_SIZE
#   num_sides - expected to be an integer > 0.
#       Default value is DEFAULT_SUCCESS_THRESHOLD
# Return Value: The number of successes obtained from a simulation of rolling an num_dice exploding dice with
#               num_sides sides and when a success is any roll of success_threshold or higher.
def roll_exploding_dice(num_dice=1, num_sides=DEFAULT_DIE_SIZE, success_threshold=DEFAULT_SUCCESS_THRESHOLD):
    total_successess = 0

    # Roll num_dice and count successes.
    for i in range(1,num_dice):
        total_successess += roll_exploding_die(num_sides, success_threshold)

    return total_successess

if __name__ == "__main__":
    print('Program running')
    for i in range(1, 10):
        print("Rolled %s successes" % roll_exploding_dice(3))
