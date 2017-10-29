"""
Exploding Dice

Written by Jesse Harder, Copyright 2017

This program contains code for modeling success probabilities for rolling exploding dice in ways akin to that of the
Burning Wheel test system.
"""

from DistributionThread import *
import export


NUM_TESTS = 1000000
MAX_DICE = 15

if __name__ == "__main__":
    print('--- Program Running ---')
    threads = []
    results = []

    # Create and run all the threads
    for i in range(1, MAX_DICE+1):
        new_thread = DistributionThread(i, i, NUM_TESTS)
        new_thread.start()
        threads.append(new_thread)

    # Wait for all of the threads to finish.
    for thread in threads:
        thread.join()

    # Gather the results
    max_dist_length = 0
    for i in range(0, MAX_DICE):
        thread = threads[i]
        dist = thread.distribution.copy()
        if len(dist) > max_dist_length:
            max_dist_length = len(dist)
        results.append(dist)

    # Tweak the results so all distributions are the same length
    for dist in results:
        ensure_distribution_length(dist, max_dist_length, 1)

    # Print Distributions
    for i in range(0,MAX_DICE):
        print("Printing results for %s dice:" % (i+1))
        print_distribution(results[i], 'f')

    export.distribution_list_to_csv(results)
