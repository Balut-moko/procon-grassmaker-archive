#!/usr/bin/env python3

def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    def dfs(v, p):
        '''
        頂点：n
        辺：n-1
        '''
        from collections import deque

        cost = [0] * n
        stack = deque([])
        stack.append([v, p])  # root
        while stack:
            v, p = stack.pop()
            if p != -1:
                cost[v] = cost[p] + 1
            for e in graph[v]:
                if e == p:
                    continue
                stack.append([e, v])
        max_cost = max(cost)
        maxV = cost.index(max_cost)
        return maxV, max_cost

    maxV, max_cost = dfs(0, -1)
    maxV, max_cost = dfs(maxV, -1)
    print(max_cost + 1)


if __name__ == "__main__":
    main()
