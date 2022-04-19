from sys import stdin

readline = stdin.readline
s = readline()[:-1]

for i in range(10):
    if str(i) not in s:
        print(i)
