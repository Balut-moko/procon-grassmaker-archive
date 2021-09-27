from sys import stdin

readline = stdin.readline
n = int(readline())
s = sorted(int(readline()) for _ in [0] * n)
sum_s = sum(s)
for i in range(n):
    if sum_s % 10 != 0:
        print(sum_s)
        exit()
    if s[i] % 10 != 0:
        sum_s -= s[i]
print(0)
