from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_sorted = sorted(a)
for i in range(n):
    if a[i] == a_sorted[-2]:
        ans = i + 1
print(ans)
