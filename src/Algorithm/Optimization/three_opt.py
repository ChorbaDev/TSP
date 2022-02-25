from time import process_time

from src.utils.help import routeLength


# Complexity of O(n^3) for 1 iteration

def reverse_segment_if_better(distance, tour, i, j, k):
    # reversing tour[i:j] if it make the tour shorter
    # Given tour [...A-B...C-D...E-F...]

    A, B, C, D, E, F = tour[i - 1], tour[i], tour[j - 1], tour[j], tour[k - 1], tour[k % len(tour)]
    # why k % n ? because when we reach the last element "n-1" n is out of bound
    # so we F represents the first element of our tour
    # [F..A-B...C-D...E]
    #
    # we try all the possibilities and we return the first optimized tour
    d0 = distance[(A, B)] + distance[(C, D)] + distance[(E, F)]
    #
    d1 = distance[(A, C)] + distance[(B, D)] + distance[(E, F)]
    d2 = distance[(A, B)] + distance[(C, E)] + distance[(D, F)]
    d4 = distance[(F, B)] + distance[(C, D)] + distance[(E, A)]

    d3 = distance[(A, D)] + distance[(E, B)] + distance[(C, F)]
    d5 = distance[(A, D)] + distance[(B, F)] + distance[(C, E)]
    d6 = distance[(A, C)] + distance[(B, E)] + distance[(D, F)]
    d7 = distance[(A, E)] + distance[(B, D)] + distance[(C, F)]

    if d0 > d1:
        tour[i:j] = reversed(tour[i:j])
        return -d0 + d1
    elif d0 > d2:
        tour[j:k] = reversed(tour[j:k])
        return -d0 + d2
    elif d0 > d4:
        tour[i:k] = reversed(tour[i:k])
        return -d0 + d4
    elif d0 > d3:
        tmp = tour[j:k] + tour[i:j]
        tour[i:k] = tmp
        return -d0 + d3
    elif d0 > d5:
        tmp = tour[j:k] + tour[i:j]
        tour[i:k] = tmp
        return -d0 + d5
    elif d0 > d6:
        tmp = tour[j:k] + tour[i:j]
        tour[i:k] = tmp
        return -d0 + d6
    elif d0 > d7:
        tmp = tour[j:k] + tour[i:j]
        tour[i:k] = tmp
        return -d0 + d7
    return 0


def all_segments(n):
    # Generate all segments combinations
    return ((i, j, k)
            for i in range(n)
            for j in range(i + 2, n)
            for k in range(j + 2, n + (i > 0)))


def three_opt(tour, distance):
    iterations, improve, comparisons = 0, 0, 0
    t1_start = process_time()
    while True:
        iterations += 1
        delta = 0
        for (a, b, c) in all_segments(len(tour)):
            comparisons += 1
            value = reverse_segment_if_better(distance, tour, a, b, c)
            delta += value
            if value < 0:
                improve += 1
        if delta >= 0:
            break
    t1_stop = process_time()
    return tour, routeLength(distance, tour), comparisons, improve, iterations, (t1_stop - t1_start)
