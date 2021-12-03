from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_abs = [abs(val) for val in a]
a_minus = sorted([val for val in a if val < 0])
if len(a_minus) % 2 == 0:
    ans = sum(a_abs)
else:
    ans = sum(a_abs) - 2 * min(a_abs)
print(ans)
