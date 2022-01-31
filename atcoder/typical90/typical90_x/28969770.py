from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
cnt = sum([abs(a - b) for a, b in zip(a, b)])
ans = "Yes"
if k < cnt or (k - cnt) % 2 != 0:
    ans = "No"
print(ans)
