from collections import defaultdict

d = defaultdict(list)
print(d)
keys = [1, 1, 2, 3, 2]

for k in keys:
    if k < 3:
        d[k].append(k * 2)


        
