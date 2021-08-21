from sys import stdin
from itertools import permutations
readline = stdin.readline
s, k = readline().split()
s = sorted(s)
k = int(k) - 1
li = sorted(set(permutations(s)))

print(*li[k], sep='')
