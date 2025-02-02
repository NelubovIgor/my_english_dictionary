from typing import Any
from itertools import zip_longest
import inspect


def outer(x):
    y = 1
    def inner():
        return x + y
    return inspect.getclosurevars(inner).nonlocals

print(outer(2))

class A:
    def __enter__(self): return self
    def __exit__(self, *args): return True
    def __call__(self): return ValueError

with A() as a:
    a()
# print("OK")

a = [1, 2]
b = [3, 4, 5]
c = list(zip_longest(a, b, fillvalue=0))

# print(c)

def safe_int(x: Any) -> tuple[bool, int]:
    try:
        return True, int(x)
    except:
        return False, 0
    
# print([safe_int(x) for x in ['1', 'a', '2']])
