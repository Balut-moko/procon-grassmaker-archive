from collections import Counter, deque
from sys import stdin

readline = stdin.readline
s = list(readline()[:-1])
t = list(readline()[:-1])

s_cnt = Counter(s)
t_cnt = Counter(t)
s_at = s_cnt["@"]
t_at = t_cnt["@"]


for k, v in s_cnt.items():
    if k in "atcoder@":
        continue
    if t_cnt[k] != v:
        print("No")
        exit()
for k, v in t_cnt.items():
    if k in "atcoder@":
        continue
    if s_cnt[k] != v:
        print("No")
        exit()

for val in "atcoder":
    sc = s_cnt[val]
    tc = t_cnt[val]
    if sc < tc:
        s_at -= tc - sc
    else:
        t_at -= sc - tc
    if s_at < 0 or t_at < 0:
        print("No")
        exit()

print("Yes")
