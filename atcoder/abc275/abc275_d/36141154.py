from sys import stdin


class F_memo:
    def __init__(self) -> None:
        self.memo = {}

    def calc(self, n):
        if n == 0:
            return 1
        val = self.memo.get(n)
        if val is not None:
            return val
        self.memo[n] = self.calc(n // 2) + self.calc(n // 3)
        return self.memo[n]


readline = stdin.readline
n = int(readline())
f = F_memo()
print(f.calc(n))
