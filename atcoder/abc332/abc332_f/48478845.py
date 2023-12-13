from atcoder.lazysegtree import LazySegTree


class F:
    def __init__(self, a, b) -> None:
        self.a = a % MOD
        self.b = b % MOD


def op(x, y):
    return x + y


def mapping(f, x):
    return (f.a * x + f.b) % MOD


def composition(f, g):
    a = f.a * g.a
    b = f.a * g.b + f.b
    return F(a, b)


N, M = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
lazy = LazySegTree(
    op=op, e=0, mapping=mapping, composition=composition, id_=F(1, 0), v=A
)

for _ in range(M):
    L, R, X = map(int, input().split())
    L -= 1
    P = pow(R - L, -1, MOD)
    q = (1 - P) % MOD
    lazy.apply(L, R, F(q, P * X))

ans = [lazy.get(i) for i in range(N)]
print(*ans)
