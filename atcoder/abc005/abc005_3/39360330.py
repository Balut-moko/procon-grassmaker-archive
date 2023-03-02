from sys import stdin

readline = stdin.readline
t = int(readline())
n = int(readline())
a = list(map(int, readline().split()))
m = int(readline())
b = list(map(int, readline().split()))
used = [False] * n
cnt = [False] * m

for i in range(m):
    for j in range(n):
        if not used[j] and a[j] <= b[i] <= a[j] + t:
            used[j] = True
            cnt[i] = True
            break
print("yes" if all(cnt) else "no")
