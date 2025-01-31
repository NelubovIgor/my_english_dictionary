from collections import defaultdict
import asyncio
from operator import itemgetter

data = [(1, "c"), (2, "b"), (1, "a")]

data.sort(key=itemgetter(0, 1))
print(data)
print([x[1] for x in data])

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


        
