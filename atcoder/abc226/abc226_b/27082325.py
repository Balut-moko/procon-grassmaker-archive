from sys import stdin

readline = stdin.readline
n = int(readline())
l_set = set()
for i in range(n):
    l, *a = map(int, readline().split())
    l_set.add(tuple(a))
print(len(l_set))
