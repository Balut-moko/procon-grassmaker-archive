from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))

ans = set()
ans.add(0)

for val in p:
    tmp = ans.copy()
    for t in tmp:
        ans.add(val + t)

print(len(ans))
