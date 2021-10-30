from sys import stdin

readline = stdin.readline
n = int(readline())
a = [tuple(map(int, readline().split())) for _ in [0] * (n - 1)]

if a[0][0] == a[1][0]:
    root = a[0][0]
elif a[0][0] == a[1][1]:
    root = a[0][0]
elif a[0][1] == a[1][0]:
    root = a[0][1]
elif a[0][1] == a[1][1]:
    root = a[0][1]
else:
    print('No')
    exit()

for val in a:
    if root not in val:
        print('No')
        exit()
print('Yes')
