from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
s = readline()[:-1]

ans = ""

for i in range(n):
    if s[i] == "o" and k > 0:
        ans += "o"
        k -= 1
    else:
        ans += "x"
print(ans)
