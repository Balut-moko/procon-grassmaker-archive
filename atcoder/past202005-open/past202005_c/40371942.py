from sys import stdin

readline = stdin.readline
A, R, N = map(int, readline().split())

if R == 1:
    print(A)
    exit()

i = 1
while i <= N:
    ans = A * pow(R, i - 1)
    if ans>10**9:
        print("large")
        exit()
    i += 1
print(ans)