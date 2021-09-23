from sys import stdin
from collections import Counter
readline = stdin.readline
n, m = map(int, readline().split())
a = Counter(map(int, readline().split()))
ans = '?'
if n // 2 < a.most_common()[0][1]:
    ans = a.most_common()[0][0]
    if 1 < len(a) and a.most_common()[0][0] == a.most_common()[1][0]:
        ans = '?'
print(ans)
