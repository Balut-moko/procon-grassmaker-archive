from sys import stdin
from collections import defaultdict
readline = stdin.readline
n = int(readline())
num_dict = defaultdict(int)
for _ in range(n):
    a = int(readline())
    if num_dict[a] == 1:
        num_dict[a] -= 1
    else:
        num_dict[a] += 1
print(sum(num_dict.values()))
