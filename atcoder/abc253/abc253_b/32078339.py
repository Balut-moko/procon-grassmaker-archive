from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]
flg = True
for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            if flg:
                start = (i, j)
                flg = False
            else:
                end = (i, j)
print(abs(start[0] - end[0]) + abs(start[1] - end[1]))
