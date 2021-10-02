from sys import stdin
from itertools import accumulate
readline = stdin.readline
n = int(readline())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]
day_set = set()
for a, b in ab:
    day_set.add(a)
    day_set.add(a + b)
day_li = sorted(list(day_set))
day_comp = {v: i for i, v in enumerate(day_li)}
day_comp_re = {i: v for i, v in enumerate(day_li)}

login = [0] * (n * 2)

for a, b in ab:
    login[day_comp[a]] += 1
    login[day_comp[a + b]] -= 1

login_cumsum = list(accumulate(login))

ans = [0] * (n + 1)
for i in range(len(day_li) - 1):
    ans[login_cumsum[i]] += day_comp_re[i + 1] - day_comp_re[i]
print(*ans[1:])
