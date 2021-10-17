from sys import stdin

readline = stdin.readline
s = readline()[:-1]
ans_min = s
ans_max = s
for i in range(len(s)):
    s = s[-1] + s[:-1]
    ans_min = min(ans_min, s)
    ans_max = max(ans_max, s)
print(ans_min)
print(ans_max)
