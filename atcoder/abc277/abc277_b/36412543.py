from sys import stdin

readline = stdin.readline
n = int(readline())
s = [readline()[:-1] for _ in [0] * n]

s_set = set()
ans = "Yes"
for i in range(n):
    if s[i] in s_set:
        ans = "No"
        break
    s_set.add(s[i])
    if s[i][0] not in ("H", "D", "C", "S"):
        ans = "No"
        break
    if s[i][1] not in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"):
        ans = "No"
        break
print(ans)
