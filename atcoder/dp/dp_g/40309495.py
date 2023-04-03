from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
readline = stdin.readline
n, m = map(int, readline().split())

in_cnt = defaultdict(int)
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    in_cnt[b] += 1

length = [-1] * n


def calc(i):
    if length[i] != -1:
        return length[i]
    length[i] = 0
    for e in graph[i]:
        length[i] = max(length[i], calc(e) + 1)
    return length[i]


for i in range(n):
    if in_cnt[i] == 0:
        calc(i)

print(max(length))
