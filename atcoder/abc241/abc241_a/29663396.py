from sys import stdin

readline = stdin.readline
a = list(map(int, readline().split()))
ans = 0
for _ in range(3):
    ans = a[ans]
print(ans)
