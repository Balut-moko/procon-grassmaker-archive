from sys import stdin
from itertools import permutations

readline = stdin.readline
container = list(map(int, readline().split()))
bag = list(map(int, readline().split()))
ans = 0
for val in permutations(bag, 3):
    tmp = 1
    for i in range(3):
        tmp *= container[i] // val[i]
    ans = max(ans, tmp)
print(ans)
