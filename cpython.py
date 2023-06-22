import argparse
import importlib
from contextlib import contextmanager

import memory_profiler


@contextmanager
def timeit(results: list):
    import time
    start = time.time()
    yield
    results.append(time.time() - start)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=str)
    parsed = parser.parse_args()

    module = importlib.import_module(parsed.m)
    avgs = []
    r = 10
    for i in range(r):
        with timeit(avgs):
            extra, callable_, args = module.main()
            callable_(*args)

    mem = memory_profiler.memory_usage((module.main, ), max_usage=True, max_iterations=r)
    print(f"{module.name};{extra};{sum(avgs) / len(avgs)};{mem}".replace(".", ","))