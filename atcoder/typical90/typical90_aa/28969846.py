from sys import stdin

readline = stdin.readline
n = int(readline())
users = set()
for i in range(n):
    s = readline()[:-1]
    if s not in users:
        print(i + 1)
    users.add(s)
