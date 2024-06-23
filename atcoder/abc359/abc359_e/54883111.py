from atcoder.lazysegtree import LazySegTree


class RSQ_and_RUQ(LazySegTree):
    """
    区間和取得
    区間更新
    ele = (value, size)
    要素数:N の lst で初期化
    """

    INF = 1 << 63
    ID = INF
    id_ = ID
    e = (0, 0)

    def __init__(self, N: int) -> None:
        lst = [(0, 1) for _ in range(N)]
        super().__init__(
            self._op, self.e, self._mapping, self._composition, self.id_, lst
        )

    def _op(self, ele1, ele2):
        return (ele1[0] + ele2[0], ele1[1] + ele2[1])

    def _mapping(self, func, ele):
        if func != self.ID:
            ele = list(ele)
            ele[0] = func * ele[1]
            ele = tuple(ele)
        return ele

    def _composition(self, func_upper, func_lower):
        if func_upper == self.ID:
            return func_lower
        else:
            return func_upper


N = int(input())
H = list(map(int, input().split()))
seg = RSQ_and_RUQ(N)
stack = []


ans = [0] * N
for i in range(N):
    idx = -1
    while stack:
        tmp = stack[-1]
        if H[tmp] >= H[i]:
            idx = tmp
            break
        stack.pop()
    seg.apply(idx + 1, i + 1, H[i])
    pre_full = seg.prod(0, i + 1)

    ans[i] = pre_full[0] + 1
    stack.append(i)
print(*ans)
