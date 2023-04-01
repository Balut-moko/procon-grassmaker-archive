from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
a = list(map(int, readline().split()))
a_set = set(a)

flag = False
for val in a:
    if x + val in a_set:
        flag = True
print("Yes" if flag else "No")
