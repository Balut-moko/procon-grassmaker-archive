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


def seg_func(x, y):
    return max(x, y)


N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

st = SegTree([0] * (N + 1), lambda x, y: max(x, y), 0)

for i in range(N):
    x = st.query(0, H[i])
    st.update(H[i], x + A[i])

print(st.query(0, N + 1))
