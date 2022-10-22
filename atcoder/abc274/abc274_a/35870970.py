from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
ans = b / a
ans = round(ans + 0.00005, 3)
ans = str(ans) + "0000000"
print(ans[:5])
