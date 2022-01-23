from sys import stdin
from collections import Counter

readline = stdin.readline
n = int(readline())
a = Counter(map(int, readline().split()))
print(a.most_common()[-1][0])
