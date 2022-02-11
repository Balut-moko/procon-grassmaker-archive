from sys import stdin
from collections import defaultdict

readline = stdin.readline
n = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
C = list(map(int, readline().split()))

a_mod_dict = defaultdict(int)
b_mod_dict = defaultdict(int)
c_mod_dict = defaultdict(int)

for a, b, c in zip(A, B, C):
    a_mod_dict[a % 46] += 1
    b_mod_dict[b % 46] += 1
    c_mod_dict[c % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += a_mod_dict[i] * b_mod_dict[j] * c_mod_dict[k]
print(ans)
