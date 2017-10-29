"""
A class for generating cumulative distributions for n dice on its own thread.
"""

import threading
from distributions import *


class DistributionThread(threading.Thread):
    def __init__(self, thread_id, num_dice, num_tests):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.num_dice = num_dice
        self.num_tests = num_tests
        self.distribution = [0]

    def run(self):
        dist = distribution_for_n_dice(self.num_dice, self.num_tests)
        self.distribution = cumulative_distribution(dist)
        print("Finished distribution for %s dice." % self.num_dice)
