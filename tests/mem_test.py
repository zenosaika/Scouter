import time

M1_AIR_BASELINE = 6
DURATION_IN_SECOND = 15

# very large array test
def mem_test():
    start = time.time()
    cnt = 0

    while time.time() - start < DURATION_IN_SECOND:
        # memory allocation & delete
        lst = ['A'] * 10**8 * 5
        del lst

        cnt += 1

    score_relative_to_m1_air = cnt / M1_AIR_BASELINE * 100
    
    return score_relative_to_m1_air
