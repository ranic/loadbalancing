import sys
import random
from math import floor

def percentile(arr, p):
    return sorted(arr)[int(len(arr)*p/100.0)]

def stats(arr):
    return (min(arr), percentile(arr, 10), percentile(arr, 25), percentile(arr, 50), percentile(arr, 75), percentile(arr, 90), max(arr))


# Work cost distributions (returns an integer >= 1)

def one():
    return 1

def powerlaw():
    return floor(random.paretovariate(5))


def uniform(inputs):
    N = len(inputs)
    bins = [0.0 for _ in xrange(N)]
    for i in xrange(N):
        bins[random.randint(0, N-1)] += inputs[i]
    return stats(bins)

def pow2(inputs):
    N = len(inputs)
    bins = [0.0 for _ in xrange(N)]
    for i in xrange(N):
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)
        if bins[a] < bins[b]:
            bins[a] += inputs[i]
        else:
            bins[b] += inputs[i]
    return stats(bins)

def pow3(inputs):
    N = len(inputs)
    bins = [0.0 for _ in xrange(N)]
    for i in xrange(N):
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)
        c = random.randint(0, N-1)
        _min = min(bins[a], bins[b], bins[c])
        for _bin in [a, b, c]:
            if bins[_bin] == _min:
                bins[_bin] += inputs[i]
                break

    return stats(bins)


N = 100 * 1000
print "Testing with {} bins and balls".format(N)
row_format ="{:>12}" * 9
print row_format.format("balancing_fn", "cost_fn", "min", "p10", "p25", "p50", "p75", "p90", "max")
for costfn in [one, powerlaw]:
    inputs = [costfn() for _ in xrange(N)]
    for distfn in [uniform, pow2, pow3]:
        print row_format.format(distfn.__name__, costfn.__name__, *distfn(inputs))
