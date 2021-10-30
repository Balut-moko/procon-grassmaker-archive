from sys import stdin


readline = stdin.readline
n, q = map(int, readline().split())

next_p = [[] for _ in range(n + 1)]
from_p = [[] for _ in range(n + 1)]

for _ in range(q):
    c, *xy = map(int, readline().split())

    if c == 1:
        next_p[xy[0]].append(xy[1])
        from_p[xy[1]].append(xy[0])
    elif c == 2:
        next_p[xy[0]].clear()
        from_p[xy[1]].clear()
    else:
        idx = xy[0]
        parent = from_p[idx]
        while parent:
            idx = parent[0]
            parent = from_p[parent[0]]
        val = [idx]
        child = next_p[idx]
        while child:
            val.append(child[0])
            child = next_p[child[0]]
        print(len(val), *val)
