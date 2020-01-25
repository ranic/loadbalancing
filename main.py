import sys
import random
from math import floor

def percentile(arr, p):
    return sorted(arr)[int(len(arr)*p/100.0)]

def stats(arr):
    return (min(arr), percentile(arr, 25), percentile(arr, 50), percentile(arr, 75), max(arr))


# Work cost distributions (returns an integer >= 1)

def one():
    return 1

def powerlaw():
    return floor(random.paretovariate(5))


def uniform(N, costfn):
    bins = [0.0 for _ in xrange(N)]
    for _ in xrange(N):
        bins[random.randint(0, N-1)] += costfn()
    return stats(bins)

def pow2(N, costfn):
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


N = 100 * 1000
print "Testing with {} bins and balls".format(N)
row_format ="{:>12}" * 7
print row_format.format("balancing_fn", "cost_fn", "min", "p25", "p50", "p75", "max")
for distfn in [uniform, pow2]:
    for costfn in [one, powerlaw]:
        print row_format.format(distfn.__name__, costfn.__name__, *distfn(N, costfn))
