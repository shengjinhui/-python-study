from random import randint

from urllib3.connectionpool import xrange

data = [1, 5, 3, 5, -1, -2, -5]
res = []
for x in data:
    if x >= 0:
        res.append(x)

print(res)

res2 = []
res2 = filter(lambda x: x > 0, data)
print(res2)

# data2 = [randint(-10, 10) for _ in xrange(10