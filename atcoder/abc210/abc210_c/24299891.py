from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
c = list(map(int, readline().split()))
ans = 0
kinds = dict()
for i in range(k):
    if c[i] not in kinds:
        kinds[c[i]] = 1
    else:
        kinds[c[i]] += 1
    ans = max(ans, len(kinds))
for i in range(n - k):
    if kinds[c[i]] == 1:
        kinds.pop(c[i])
    else:
        kinds[c[i]] -= 1
    if c[i + k] not in kinds:
        kinds[c[i + k]] = 1
    else:
        kinds[c[i + k]] += 1
    ans = max(ans, len(kinds))
print(ans)
