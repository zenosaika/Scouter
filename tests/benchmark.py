def benchmark(func, n_warm_up, n_test):

    # warm up n times
    for _ in range(n_warm_up):
        func()

    # real test
    score_summation = 0
    for _ in range(n_test):
        score_summation += func()
    average_score = score_summation / n_test

    return average_score