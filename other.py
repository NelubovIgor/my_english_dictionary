from collections import defaultdict
import asyncio
from operator import itemgetter
from itertools import groupby
from dataclasses import dataclass, field
from functools import lru_cache, partial
import heapq
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    BLUE = 2
    GREEN = auto()

print([c.value for c in Color])

nums = [4, 1, 7, 3]
heapq.heapify(nums)

# print([heapq.heappop(nums) for _ in range(2)])
# print(nums)

def foo(x=[]):
    x.append(1)
    return len(x)

# print(foo())
# print(foo())
# print(foo([]))

def add(x, y=0, z=0): return x + y + z
f1 = partial(add, 1)
f2 = partial(f1, y = 2)
# print(f"{f1(2)}, {f2(z=3)}")

class Descriptor:
    def __get__(self, obj, type=None):
        return 42
    
class A:
    x = Descriptor()
    def __getattr__(self, name):
        return 21
    
a = A()
# print(f"{a.x}, {a.y}")

@lru_cache
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

r = [fib(i) for i in [3, 3, 4]]
# print(r)

@dataclass
class Box:
    items: list = field(default_factory=list)
    size: int = 0

b1 = Box()    
b2 = Box()
b1.items.append(1)
# print(f"{b1.items}, {b2.items}")

data = [1, 1, 2, 3, 3, 3, 2]
res = []
for k, g in groupby(sorted(data)):
    res.append(len(list(g)))
# print(res)

data1 = [(1, "c"), (2, "b"), (1, "a")]
data1.sort(key=itemgetter(0, 1))
# print([x[1] for x in data1])

async def double(x):
    return x * 2

async def main():
    tasks = [double(i) for i in range(3)]
    r = await asyncio.gather(*tasks)
    # print(r)

asyncio.run(main())

d = defaultdict(list)

keys = [1, 1, 2, 3, 2]

for k in keys:
    if k < 3:
        d[k].append(k * 2)


        
