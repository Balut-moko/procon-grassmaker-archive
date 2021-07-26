from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
odd = 0
even = 0
for i in range(n):
    s = readline()[:-1]
    if s.count('1') % 2 == 0:
        even += 1
    else:
        odd += 1
print(odd * even)
