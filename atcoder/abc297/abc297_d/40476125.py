from sys import stdin

readline = stdin.readline
A, B = map(int, readline().split())
cnt = 0
while A != B:
    if A < B:
        A, B = B, A
    if A % B == 0:
        cnt += A // B - 1
        break
    tmp = A // B
    A -= tmp * B
    cnt += tmp

print(cnt)
