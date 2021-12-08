import time
from itertools import pairwise


def time_it_and_evaluate(method):
    def wrapper_method(*arg, **kw):
        start = time.perf_counter_ns()
        ret = method(*arg, **kw)
        print(f'{method.__name__} => `{ret}` [{(time.perf_counter_ns() - start) / 1e3 :2.2f} ms]')
        return ret

    return wrapper_method


def triplewise(iterable):
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def groupify(nums, count):
    for i in range(len(nums[::count])):
        yield int(''.join(nums[i + c] for c in range(count)))


def read_all_lines(file_name: str) -> list[str]:
    with open(file_name, 'r') as f:
        read_data = f.readlines()
    return read_data
