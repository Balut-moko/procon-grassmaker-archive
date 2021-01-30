#!/usr/bin/env python3

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def main():
    n = int(input())
    A = list(map(int, input().split()))
    bit = Bit(n)
    ans = 0
    for i, a in enumerate(A):
        ans += i - bit.sum(a + 1)
        bit.add(a, 1)
    print(ans)
    for k in range(1, n):
        ans += n - 1 - A[k - 1] * 2
        print(ans)


if __name__ == "__main__":
    main()
