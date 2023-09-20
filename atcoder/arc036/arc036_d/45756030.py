from atcoder.dsu import DSU


n, q = map(int, input().split())

uf = DSU(2 * n)

for _ in range(q):
    w, x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    if w == 1:
        if z % 2 == 0:
            uf.merge(x, y)
            uf.merge(x + n, y + n)
        else:
            uf.merge(x + n, y)
            uf.merge(x, y + n)
    else:
        print("YES" if uf.same(x, y) else "NO")
