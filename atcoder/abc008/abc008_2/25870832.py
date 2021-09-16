from sys import stdin
from collections import Counter
readline = stdin.readline
n = int(readline())
print(Counter([readline()[:-1] for _ in [0] * n]).most_common()[0][0])
