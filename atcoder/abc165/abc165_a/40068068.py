from sys import stdin

readline = stdin.readline
k = int(readline())
a, b = map(int, readline().split())

print("OK" if a // k < b // k or a % k == 0 else "NG")
