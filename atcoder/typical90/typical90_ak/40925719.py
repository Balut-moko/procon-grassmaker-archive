from sys import stdin


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


readline = stdin.readline
w, n = map(int, readline().split())


def seg_func(x, y):
    return max(x, y)


seg = SegTree([-1 << 60] * (w + 1), seg_func, -1 << 60)
lrv = [tuple(map(int, readline().split())) for _ in [0] * n]

dp = [-1 << 60] * (w + 1)
dp[0] = 0
seg.update(0, 0)

for l, r, v in lrv:
    for j in range(l, r):
        dp[j] = max(dp[j], seg.query(0, j - l + 1) + v)
    for j in range(r, w + 1):
        dp[j] = max(dp[j], seg.query(j - r, j - l + 1) + v)

    for j in range(w + 1):
        seg.update(j, dp[j])


print(dp[w] if dp[w] > 0 else -1)
