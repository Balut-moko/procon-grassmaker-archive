import string

N = int(input())
S = input()
di = {chr(ord("a") + i): chr(ord("a") + i) for i in range(26)}
az = string.ascii_lowercase
Q = int(input())
for _ in range(Q):
    c, d = input().split()
    az = az.replace(c, d)

di = {chr(ord("a") + i): az[i] for i in range(26)}
ans = ""
for s in S:
    ans += di[s]

print(ans)
