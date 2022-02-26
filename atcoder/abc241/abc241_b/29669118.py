from sys import stdin
from collections import defaultdict

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
a_dict = defaultdict(int)
for val in a:
    a_dict[val] += 1
for val in b:
    a_dict[val] -= 1
ans = "Yes"
for val in a_dict.values():
    if val < 0:
        ans = "No"
print(ans)
