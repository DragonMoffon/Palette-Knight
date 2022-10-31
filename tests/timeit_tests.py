from random import random
from timeit import timeit

source = [random() for _ in range(100)]
source_set = set(source)

list_r = timeit(lambda: list(source_set), number=100000)
tuple_r = timeit(lambda: tuple(source), number=100000)

print(f"list time: {list_r}, tuple time: {tuple_r}")
