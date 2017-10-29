"""
export.py

This file contains functions writing distributions into files to be preserved.

Written by Jesse Harder

Format is

dice
|
V
dice\successes,   0,      1,      2, ... (< - numer of successes)
1,                P(0),   P(≤1),  P(≤2),
2,                P(0),   P(≤1),  P(≤2),
3,                P(0),   P(≤1),  P(≤2),
"""


def distribution_list_to_csv(distributions):
    print('Writing results to file')
    csv_file = open('results.csv', 'w')
    num_entries = len(distributions)
    entry_length = len(distributions[0])
    print('Entry length - %s' % entry_length)

    # Write header
    csv_file.write("dice\\successes")
    for i in range(0,entry_length):
        csv_file.write(",%s" % i)
    csv_file.write("\n")

    # Write results
    for i in range(0, num_entries):
        csv_file.write(str(i+1))
        dist = distributions[i]
        for j in range(0, entry_length):
            csv_file.write(',%.4f' % dist[j])
        if i < num_entries-1:
            csv_file.write('\n')
