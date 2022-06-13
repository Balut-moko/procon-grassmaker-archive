from collections import defaultdict
from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]

di_ts = defaultdict(set)
di_st = defaultdict(set)

for i, j in zip(s, t):
    di_ts[j].add(i)
    di_st[i].add(j)

ans = "Yes"
for val in di_ts.values():
    if len(val) > 1:
        ans = "No"
        break
for val in di_st.values():
    if len(val) > 1:
        ans = "No"
        break
print(ans)
