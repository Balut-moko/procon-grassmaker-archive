from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_even = [val for val in a if val % 2 == 0]
print(*a_even)
