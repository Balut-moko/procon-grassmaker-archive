from sys import stdin
from collections import defaultdict

readline = stdin.readline
s = readline()[:-1]
d = defaultdict(int)
upper, lower = False, False

for val in s:
    d[val] += 1
    lower = lower or val.islower()
    upper = upper or val.isupper()

if max(d.values()) == 1 and lower and upper:
    ans = "Yes"
else:
    ans = "No"
print(ans)
