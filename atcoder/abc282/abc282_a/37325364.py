from sys import stdin

readline = stdin.readline
K = int(readline())
ans = ""
for i in range(K):
    ans += chr(ord("A") + i)
print(ans)
