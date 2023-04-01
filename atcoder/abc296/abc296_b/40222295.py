from sys import stdin

readline = stdin.readline
s = [readline()[:-1] for _ in [0] * 8]

for i in range(8):
    for j in range(8):
        if s[i][j] == "*":
            print(chr(ord("a") + j) + str(8 - i))
