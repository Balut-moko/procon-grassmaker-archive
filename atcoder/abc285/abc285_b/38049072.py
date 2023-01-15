from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

for i in range(1, n):
    for k in range(n - i):
        if s[k] == s[k + i]:
            print(k)
            break
    else:
        print(n - i)
