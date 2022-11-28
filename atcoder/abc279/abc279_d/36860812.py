from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())


def ternary_search_integer(left: int, right: int):
    def solve(x: int):
        return b * x + a / ((x + 1) ** 0.5)

    while left + 2 < right:
        c1 = left + (right - left) // 3
        c2 = right - (right - left) // 3
        if solve(c1) < solve(c2):
            right = c2
        else:
            left = c1
    return min(solve(left), solve(left + 1), solve(left + 2))


print(ternary_search_integer(0, 10**18 + 1))
