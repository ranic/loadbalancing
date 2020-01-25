import sys
import random

def percentile(arr, p):
    return sorted(arr)[int(len(arr)*p/100.0)]

def stats(arr):
    return (min(arr), percentile(arr, 25), percentile(arr, 50), percentile(arr, 75), max(arr))


def simulate_uniform_random(N):
    bins = [0.0 for _ in xrange(N)]
    for _ in xrange(N):
        bins[random.randint(0, N-1)] += 1
    return stats(bins)

def simulate_pow_2(N):
    bins = [0.0 for _ in xrange(N)]
    for _ in xrange(N):
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)
        if bins[a] < bins[b]:
            bins[a] += 1
        else:
            bins[b] += 1
    return stats(bins)

row_format ="{:>10}" * 6
for fn in [simulate_uniform_random, simulate_pow_2]:
    print "Testing method: {}".format(fn.__name__)
    print row_format.format("N", "min", "p25", "p50", "p75", "max")
    for N in [10, 100, 1000, 10000, 100000]:
        print row_format.format(N, *fn(N))
    

