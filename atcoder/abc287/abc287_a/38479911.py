from sys import stdin

readline = stdin.readline
n = int(readline())
s = [readline()[:-1] for _ in [0] * n]

cnt = sum([val.count("F") for val in s])
print("Yes" if cnt > n // 2 else "No")
