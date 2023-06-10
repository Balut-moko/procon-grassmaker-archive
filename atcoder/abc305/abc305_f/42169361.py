from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(100000)


def move(arg):
    print(f"{arg}", flush=True)
    res = readline().split()
    if res[0] in ("-1", "OK"):
        exit()
    cnt = int(res[0])
    li = []
    for i in range(cnt):
        li.append(int(res[i + 1]))
    return cnt, li


readline = stdin.readline
n, m = map(int, readline().split())
graph = defaultdict(set)
used = [False] * (n + 1)
used[1] = True
cnt, *li = map(int, readline().split())
for val in li:
    graph[1].add(val)
    graph[val].add(1)


def dfs(i, pre):
    cnt, li = move(i)
    for val in li:
        graph[i].add(val)
        graph[val].add(i)
    used[i] = True
    for w in graph[i]:
        if used[w] is True:
            continue
        dfs(w, i)
    move(pre)
    return


for w in graph[1]:
    dfs(w, 1)
