from itertools import combinations, permutations
from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

for val in permutations(s, len(s)):
    t = "".join(val)
    if s != t and s != t[::-1]:
        print(t)
        exit()
print("None")
