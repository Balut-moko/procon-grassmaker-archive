from sys import stdin
from collections import defaultdict


readline = stdin.readline
h, w = map(int, readline().split())
p = [tuple(map(int, readline().split())) for _ in [0] * h]
# p = list(zip(*p))
ans = 0
for i in range(2 ** h):
    tmp_ans = defaultdict(int)
    tmp_max = 0
    for j in range(w):
        cnt = 0
        num_set = set()
        for k in range(h):
            if (i >> k) & 1:
                cnt += 1
                num_set.add(p[k][j])
        if len(num_set) == 1:
            num = num_set.pop()
            tmp_ans[num] += cnt
            tmp_max = max(tmp_max, tmp_ans[num])
    ans = max(ans, tmp_max)

print(ans)
