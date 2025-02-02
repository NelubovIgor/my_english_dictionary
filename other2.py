from typing import Any
from itertools import zip_longest

a = [1, 2]
b = [3, 4, 5]
c = list(zip_longest(a, b, fillvalue=0))

print(c)

def safe_int(x: Any) -> tuple[bool, int]:
    try:
        return True, int(x)
    except:
        return False, 0
    
# print([safe_int(x) for x in ['1', 'a', '2']])
