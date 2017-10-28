# TODO: Add file header for multithreading.

import threading
from distributions import *

NUM_THREADS = 100


class RollingThread(threading.Thread):
    # Class variables.
    distribution = [0]
    distribution_lock = threading.Lock()
    roll_counter = 0
    counter_lock = threading.Lock()

    def __init__(self, thread_id, die_size, num_tests):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.die_size = die_size
        self.num_tests = num_tests

    def run(self):
        while True:
            # --- Begin Critical Region 1 ---
            RollingThread.counter_lock.acquire()
            # Check if more tests need to be done.
            if RollingThread.roll_counter >= self.num_tests:
                RollingThread.counter_lock.release()
                break
            else:
                RollingThread.roll_counter += 1
                RollingThread.counter_lock.release()
            # --- End Critical Region 1 ---

            successes = roll_exploding_dice(self.die_size)

            self.add_successes_to_distribution(successes)

    def add_successes_to_distribution(self, successes):
        # --- Begin Critical Region 2 ---
        RollingThread.distribution_lock.acquire()

        # Expand list if necessary.
        if len(RollingThread.distribution) <= successes:
            RollingThread.distribution.extend([0] * (successes - len(RollingThread.distribution) + 1))

        RollingThread.distribution[successes] += 1

        RollingThread.distribution_lock.release()
        # --- End Critical Region 2 ---

    @staticmethod
    def reset():
        RollingThread.distribution = [0]
        roll_counter = 0

    @staticmethod
    def run_tests(die_size, num_tests, num_threads=NUM_THREADS):
        RollingThread.reset()

        threads = []
        for i in range(1, num_threads):
            thread = RollingThread(i, die_size, num_tests)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        RollingThread.distribution_lock.acquire()

        new_distribution = RollingThread.distribution.copy()

        RollingThread.distribution_lock.release()

        return new_distribution


# Function: distribution_for_n_dice
# Parameters:
#   n - number of dice rolled for each tests. Expected to be an integer > 0.
# Return Value: a list containing number of times N successes was rolled at index N of the list.
# Note: Uses multithreading for increased speed.
def distribution_for_n_dice(n, num_tests):
    return RollingThread.run_tests(n, num_tests)
