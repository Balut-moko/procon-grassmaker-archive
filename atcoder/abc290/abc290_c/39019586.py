from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))

a.sort()
cnt = 0
for val in a:
    if cnt == k:
        break
    if val == cnt:
        cnt += 1
    elif val < cnt:
        continue
    else:
        break
print(cnt)
