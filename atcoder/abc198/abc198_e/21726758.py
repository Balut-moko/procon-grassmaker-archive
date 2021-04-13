#!/usr/bin/env python3
from collections import deque


def main():
    n = int(input())
    c = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    color = [0] * (10**5 + 1)
    for i in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    stack = deque([])
    stack.append([0, -1])
    ans = []
    while stack:
        v, p = stack.pop()
        if v >= 0:
            color[c[v]] += 1
            if color[c[v]] == 1:
                ans.append(v + 1)
            for e in graph[v]:
                if e == p:
                    continue
                stack.append([-e, v])
                stack.append([e, v])
        else:
            color[c[-v]] -= 1
    ans = sorted(ans)
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
