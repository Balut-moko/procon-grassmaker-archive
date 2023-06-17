from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(lambda x: int(x) - 1, readline().split()))

ans = [0] * n
cnt = [0] * n

for i, val in enumerate(a):
    if cnt[val] == 0:
        cnt[val] += 1
    elif cnt[val] == 1:
        ans[val] = i
        cnt[val] += 1
    else:
        continue

ans = [(val, i + 1) for i, val in enumerate(ans)]
ans.sort()
ans = [i for val, i in ans]
print(*ans)
