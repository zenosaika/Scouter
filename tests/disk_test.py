import os
import time

M1_AIR_BASELINE = 18
DURATION_IN_SECOND = 15

# create, write, read and delete text-file test
def disk_test():
    cnt = 0
    start = time.time()

    one_GB = "B" * 10**9

    while time.time() - start < DURATION_IN_SECOND:
        try:
            with open("disk_benchmark.txt", "w") as file:
                file.write(one_GB) # write 1 GB data

            with open("disk_benchmark.txt", "r") as file:
                _ = file.read() # read 1 GB data

            os.remove("disk_benchmark.txt") # delete file

            # finish 1 cycle -> update count
            cnt += 1

        except Exception as err:
            print(err)

    score_relative_to_m1_air = cnt / M1_AIR_BASELINE * 100

    return score_relative_to_m1_air