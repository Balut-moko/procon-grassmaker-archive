from collections import deque


def calc_tree_diameter(tree):
    def bfs(graph, root):
        dist = [None] * len(graph)
        que = deque([root])
        dist[root] = 0
        while que:
            v = que.popleft()
            d = dist[v]
            for w, c in graph[v]:
                if dist[w] is not None:
                    continue
                dist[w] = d + c
                que.append(w)
        d = max(dist)
        return dist.index(d), d

    u, _ = bfs(tree, 0)
    _, d = bfs(tree, u)
    return d


N = int(input())

graph = [[] for _ in range(N)]
total = 0
for i in range(N - 1):
    u, v, cost = map(int, input().split())
    graph[u - 1].append((v - 1, cost))
    graph[v - 1].append((u - 1, cost))
    total += cost

d = calc_tree_diameter(graph)

print(2 * total - d)
