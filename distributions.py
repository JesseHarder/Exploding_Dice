# TODO: Add file header for distributions.


from dice import *


# Function: distribution_for_n_dice
# Parameters:
#   n - number of dice rolled for each tests. Expected to be an integer > 0.
# Return Value: a list containing number of times N successes was rolled at index N of the list.
def distribution_for_n_dice(n, num_tests):
    distribution = [0]

    # Execute a large number of rolls and gather statistics for them.
    for i in range(1, num_tests):
        successes = roll_exploding_dice(n)

        # Expand list if necessary.
        ensure_distribution_length(distribution, successes+1)

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

    for i in range(0, len(distribution)):
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


# Function: ensure_distribution_length
# Parameters:
#   distribution - a distribution of the type returned by distribution_for_n_dice.
#   length - a number for the minimum length distribution must be
#   extend_val - the value to place in any new indices added when increasing array length.
# Behavior: If "distribution" is shorter than "length" extends it to "length" with "0" elements
def ensure_distribution_length(distribution, length, extend_val=0):
    if len(distribution) < length:
        distribution.extend([0] * (length - len(distribution)))