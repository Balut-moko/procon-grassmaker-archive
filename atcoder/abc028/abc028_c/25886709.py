from sys import stdin
from itertools import combinations
readline = stdin.readline
ae = list(map(int, readline().split()))
print(max(ae[4]+ae[3]+ae[0], ae[4]+ae[2]+ae[1]))
