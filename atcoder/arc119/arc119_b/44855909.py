from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
t = readline()[:-1]

if s.count("1") != t.count("1"):
    print(-1)
    exit()

a = []
b = []
for i in range(n):
    if s[i] == "0":
        a.append(i)
    if t[i] == "0":
        b.append(i)


cnt = 0
for i in range(len(a)):
    if a[i] != b[i]:
        cnt += 1

print(cnt)
