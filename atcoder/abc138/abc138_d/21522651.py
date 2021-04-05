#!/usr/bin/env python3
from collections import deque


def main():
    n, q = map(int, input().split())
    ans = [0] * n
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    for _ in range(q):
        p, x = map(int, input().split())
        ans[p - 1] += x
    stack = deque([])
    stack.appendleft([0, -1])
    while stack:
        v, p = stack.pop()
        if p != -1:
            ans[v] += ans[p]
        for e in graph[v]:
            if e == p:
                continue
            stack.appendleft([e, v])
    print(*ans)


if __name__ == "__main__":
    main()
