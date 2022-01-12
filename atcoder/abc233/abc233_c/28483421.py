from sys import stdin
from collections import defaultdict

readline = stdin.readline
n, x = map(int, readline().split())
num_dict = defaultdict(int)
num_dict[1] += 1
for _ in range(n):
    l, *a = map(int, readline().split())
    num_li = list(num_dict.keys())
    new_num_dict = defaultdict(int)
    for i in range(l):
        for num in num_li:
            new_num_dict[num * a[i]] += num_dict[num]
    num_dict = new_num_dict
print(num_dict[x])
