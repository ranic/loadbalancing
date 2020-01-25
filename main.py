import sys
import random
from math import floor

def percentile(arr, p):
    return sorted(arr)[int(len(arr)*p/100.0)]

def stats(arr):
    return (min(arr), percentile(arr, 25), percentile(arr, 50), percentile(arr, 75), max(arr))


# Work cost distributions (returns an integer >= 1)

def uniform():
    return 1

def powerlaw():
    return floor(random.paretovariate(5))


def uniformly_random(N, costfn):
    bins = [0.0 for _ in xrange(N)]
    for _ in xrange(N):
        bins[random.randint(0, N-1)] += costfn()
    return stats(bins)

def power_of_2(N, costfn):
    bins = [0.0 for _ in xrange(N)]
    for _ in xrange(N):
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)
        x = costfn()
        if bins[a] < bins[b]:
            bins[a] += x
        else:
            bins[b] += x
    return stats(bins)

row_format ="{:>10}" * 6
for fn in [uniformly_random, power_of_2]:
    for costfn in [uniform, powerlaw]:
        print "Testing {} balancing with {} cost function".format(fn.__name__, costfn.__name__)
        print row_format.format("N", "min", "p25", "p50", "p75", "max")
        for N in [10, 100, 1000, 10000, 100000]:
            print row_format.format(N, *fn(N, costfn))
