"""
Exploding Dice

Written by Jesse Harder, Copyright 2017

This program contains code for m odeling success probabilities for rolling exploding dice in ways akin to that of the
Burning Wheel test system.
"""

import distributions


NUM_TESTS = 100000


if __name__ == "__main__":
    print('--- Program Running ---')
    dist = distributions.distribution_for_n_dice(10, NUM_TESTS)
    print("Roll Distribution")
    distributions.print_distribution(dist)
    print("\nCumulative Distribution")
    distributions.print_distribution(
        distributions.cumulative_distribution(dist), 'f')
