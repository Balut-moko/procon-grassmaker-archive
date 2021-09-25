from sys import stdin

readline = stdin.readline
s = readline()[:-1]
k = int(readline())

if len(s) < k:
    print(0)
    exit()
ans = set()
for i in range(len(s) - k + 1):
    ans.add(s[i:i + k])

print(len(ans))
