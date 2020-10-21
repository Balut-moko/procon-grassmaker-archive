#!/usr/bin/env python3
import math


class SegTree:
    def __init__(self, init_val):
        n = len(init_val)
        self.ide_ele = 0
        self.num = 1 << (n - 1).bit_length()
        self.tree = [self.ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def segfunc(self, x, y):
        return math.gcd(x, y)

    def update(self, k, x):
        """
        k: index(0-index)
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, left, right):
        """
        [left, r)のsegfuncしたものを得る
        left: index(0-index)
        right: index(0-index)
        """
        res = self.ide_ele

        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


def main():
    n = int(input())
    a = list(map(int, input().split()))
    seg = SegTree(a)
    ans = -1
    for i in range(n):
        ans = max(ans, math.gcd(seg.query(0, i), seg.query(i + 1, n)))
    print(ans)


if __name__ == "__main__":
    main()
