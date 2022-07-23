from sys import stdin

readline = stdin.readline
rl, rr, bl, br = map(int, readline().split())
ans = max(min(rr, br) - max(rl, bl), 0)
print(ans)
