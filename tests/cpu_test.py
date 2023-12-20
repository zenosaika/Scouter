import time
M1_AIR_BASELINE = 1123795
DURATION_IN_SECOND = 15

# fibonacci
def cpu_test():
    cnt = 0
    n = m = 1
    start = time.time()

    while time.time() - start < DURATION_IN_SECOND:
        # calculate next fibonacci
        next_fibo = n + m
        n = m
        m = next_fibo

        # count
        cnt += 1

    score_relative_to_m1_air = cnt / M1_AIR_BASELINE * 100

    return score_relative_to_m1_air
