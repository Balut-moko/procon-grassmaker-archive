from sys import stdin
import bisect
import array
readline = stdin.readline
l, q = map(int, readline().split())
li = array.array("i", [0, l])
ans = []
for _ in [0] * q:
    c, x = map(int, readline().split())
    idx = bisect.bisect_left(li, x)
    if c == 1:
        li.insert(idx, x)
    else:
        ans.append(li[idx] - li[idx - 1])
print(*ans, sep='\n')
