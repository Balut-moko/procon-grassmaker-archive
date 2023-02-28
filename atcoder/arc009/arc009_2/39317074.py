from sys import stdin

readline = stdin.readline
b = list(readline().split())
n = int(readline())
a = [readline()[:-1] for _ in [0] * n]

aa = []
b_di = {v: str(i) for i, v in enumerate(b)}
for i in range(n):
    tmp = ""
    for val in a[i]:
        tmp += b_di[val]
    aa.append((int(tmp), i))

aa.sort()

for i in range(n):
    print(a[aa[i][1]])
