from sys import stdin

readline = stdin.readline
q, h, s, d = map(int, readline().split())
n = int(readline())
ans = 0

cost1 = min(s, h * 2, q * 4)
cost2 = min(d, s * 2, h * 4, q * 8)
div, mod = divmod(n, 2)
ans = cost2 * div + mod * cost1
print(ans)
