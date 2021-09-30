from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
t = readline()[:-1]

for i in range(n):
    ans = s[:i] + t
    if s in ans[:n]:
        print(len(ans))
        exit()
print(2 * n)
