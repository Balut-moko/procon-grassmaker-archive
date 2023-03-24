from sys import stdin

readline = stdin.readline
a, b, k = map(int, readline().split())

for i in range(max(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        k -= 1
    if k == 0:
        print(i)
        break
