from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
w = list(map(int, readline().split()))
di = defaultdict(list)
li = []
adult_max = 0
kids_max = 0
for i in range(n):
    di[w[i]].append(s[i])
    if s[i] == "1":
        adult_max += 1
    else:
        kids_max += 1


kids = 0
adult = 0
ans = max(kids_max, adult_max)
for key in sorted(di.keys()):
    li = di[key]
    for val in li:
        if val == "1":
            adult += 1
    ans = max(ans, kids + adult_max - adult)
    for val in li:
        if val == "0":
            kids += 1
    ans = max(ans, kids + adult_max - adult)
print(ans)
