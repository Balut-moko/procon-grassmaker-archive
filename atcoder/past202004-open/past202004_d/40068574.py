from itertools import product
import string
from sys import stdin
from re import search

readline = stdin.readline
s = readline()[:-1]
ans = 0
for i in range(1, 4):
    for val in product(string.ascii_lowercase + ".", repeat=i):
        val = "".join(val)
        if search(val, s):
            ans += 1
print(ans)
