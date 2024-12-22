from timing import perf_counter
def time_function(func):
    start = perf_counter()
    func()
    end = perf_counter()
    print(f'Time: {end - start:.2f}')

