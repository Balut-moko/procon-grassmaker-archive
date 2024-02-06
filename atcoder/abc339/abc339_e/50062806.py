def seg_func(x, y):
    return max(x, y)


class SegTree:
    def __init__(self, init_val, seg_func, ide_ele):
        n = len(init_val)
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [self.ide_ele] * 2 * self.num
        self.seg_func = seg_func
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.seg_func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k: index(0-index)
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.seg_func(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, left, right):
        """
        [left, r)のseg_funcしたものを得る
        left: index(0-index)
        right: index(0-index)
        """
        res = self.ide_ele

        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.seg_func(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.seg_func(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


N, D = map(int, input().split())
A = list(map(int, input().split()))

st = SegTree([0] * (5 * 10**5 + 1), seg_func, 0)

for i in range(N):
    mx = st.query(max(1, A[i] - D), min(5 * 10**5 + 1, A[i] + D + 1))
    st.update(A[i], mx + 1)

print(st.query(0, 5 * 10**5 + 1))
