from sys import stdin


def solve(rgb):
    r, g, b = rgb[0], rgb[1], rgb[2]
    ans = 1 << 30
    if (g - r) % 3 == 0:
        ans = min(ans, g)
    if (b - r) % 3 == 0:
        ans = min(ans, b)
    if (b - g) % 3 == 0:
        ans = min(ans, b)
    return ans if ans != (1 << 30) else -1


readline = stdin.readline
t = int(readline())
for i in range(t):
    rgb = sorted(map(int, readline().split()))
    print(solve(rgb))
