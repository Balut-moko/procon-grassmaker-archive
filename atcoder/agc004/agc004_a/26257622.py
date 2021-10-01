from sys import stdin

readline = stdin.readline
abc = sorted(map(int, readline().split()))
for i in range(3):
    if abc[i] % 2 == 0:
        print(0)
        exit()
print(abc[0] * abc[1])
