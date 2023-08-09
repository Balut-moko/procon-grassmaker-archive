from sys import stdin


def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False


readline = stdin.readline
n = int(readline())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]
cd = [tuple(map(int, readline().split())) for _ in [0] * n]

edges = [set() for _ in range(n)]
matched = [-1] * n

for i in range(n):
    for j in range(n):
        if ab[i][0] < cd[j][0] and ab[i][1] < cd[j][1]:
            edges[i].add(j)

print(sum(dfs(s, set()) for s in range(n)))
