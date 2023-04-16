from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
a = [int(readline()) for _ in [0] * n]

dic = defaultdict(int)

for val in a:
    dic[val] += 1
x, y = -1, -1
for i in range(1, n + 1):
    if dic[i] == 2:
        y = i
    if dic[i] == 0:
        x = i

print("Correct" if x == -1 and y == -1 else f"{y} {x}")
