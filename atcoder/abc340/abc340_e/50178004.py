class LazySegTree_RAQ:
    def __init__(self, init_val, seg_func, ide_ele):
        self.n = len(init_val)
        self.seg_func = seg_func
        self.ide_ele = ide_ele
        self.num = 1 << (self.n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num

    def g_index(self, l, r):
        L = (l + self.num) >> 1
        R = (r + self.num) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range((self.n - 1).bit_length()):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1
            R >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i - 1]
            if not v:
                continue
            self.lazy[2 * i - 1] += v
            self.lazy[2 * i] += v
            self.tree[2 * i - 1] += v
            self.tree[2 * i] += v
            self.lazy[i - 1] = 0

    def update(self, l, r, x):
        (*ids,) = self.g_index(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if r & 1:
                r -= 1
                self.lazy[r - 1] += x
                self.tree[r - 1] += x
            if l & 1:
                self.lazy[l - 1] += x
                self.tree[l - 1] += x
                l += 1
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i - 1] = self.seg_func(self.tree[2 * i - 1], self.tree[2 * i])

    def query(self, l, r):
        self.propagates(*self.g_index(l, r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if r & 1:
                r -= 1
                res = self.seg_func(res, self.tree[r - 1])
            if l & 1:
                res = self.seg_func(res, self.tree[l - 1])
                l += 1
            l >>= 1
            r >>= 1
        return res


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = 0
st = LazySegTree_RAQ([0] * (N + 1), lambda x, y: x + y, 0)
for i in range(N):
    st.update(i, i + 1, A[i])


for i in range(M):
    ball = st.query(B[i], B[i] + 1)
    st.update(B[i], B[i] + 1, -ball)
    div, mod = divmod(ball, N)
    if div > 0:
        st.update(0, N, div)
    if mod > 0:
        st.update(B[i] + 1, min(N + 1, B[i] + mod + 1), 1)
        mod -= N - B[i]
        if mod >= 0:
            st.update(0, mod + 1, 1)

ans = [st.query(i, i + 1) for i in range(N)]

print(*ans)
