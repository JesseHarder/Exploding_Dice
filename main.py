"""
Exploding Dice

Written by Jesse Harder, Copyright 2017

This program contains code for m odeling success probabilities for rolling exploding dice in ways akin to that of the
Burning Wheel test system.
"""

from random import *


DEFAULT_DIE_SIZE = 6
DEFAULT_SUCCESS_THRESHOLD = 4
NUM_TESTS = 100000


""" Dice Functions """


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


""" Distribution Functions """


# Function: distribution_for_n_dice
# Parameters:
#   n - number of dice rolled for each tests. Expected to be an integer > 0.
# Return Value: a list containing number of times N successes was rolled at index N of the list.
def distribution_for_n_dice(n):
    distribution = [0]

    # Execute a large number of rolls and gather statistics for them.
    for i in range(1, NUM_TESTS):
        successes = roll_exploding_dice(n)

        # Expand list if necessary.
        if len(distribution) <= successes:
            distribution.extend([0] * (successes - len(distribution) + 1))

        distribution[successes] += 1

    return distribution


# Function: cumulative_distribution(distribution)
# Parameters:
#   distribution - a distribution of the type returned by distribution_for_n_dice.
# Return Value: a list where index N contains sum of all vlaues at index i <= N divided by the sum of all values
#               in the list.
def cumulative_distribution(distribution):
    assert len(distribution) >= 1

    sum_dist = [0] * len(distribution)

    # Generate summed distribution and count total.
    sum_dist[0] = distribution[0]
    sum = sum_dist[0]

    for i in range(0, len(distribution)-1):
        sum_dist[i] = sum + distribution[i]
        sum += distribution[i]

    # Convert to cumulative.
    cum_dist = [x / sum for x in sum_dist]
    return cum_dist


# Function print_distribution
# Parameters:
#   distribution - a distribution of the type returned by distribution_for_n_dice.
#   form - a string to indicate printing format. Pass 'f' to get floats.
# Behavior: Prints the index, value pairs in the given list.
def print_distribution(distribution, form='s'):
    if form == 'f':
        for i in range(0,len(distribution)):
            print('%s\t-\t%.4f' % (i, distribution[i]))
    else:
        for i in range(0, len(distribution)):
            print('%s\t-\t%s' % (i, distribution[i]))


if __name__ == "__main__":
    print('--- Program Running ---')
    dist = distribution_for_n_dice(10)
    print("Roll Distribution")
    print_distribution(dist)
    print("\nCumulative Distribution")
    print_distribution(cumulative_distribution(dist), 'f')
