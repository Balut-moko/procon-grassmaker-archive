N = int(input())
A = list(map(int, input().split()))
P = [0] + list(map(lambda x: int(x) - 1, input().split()))

dep = [0] * N

for i in range(1, N):
    dep[i] = dep[P[i]] + 1

s = [0] * N

for i in range(N):
    s[dep[i]] += A[i]

for i in range(N - 1, -1, -1):
    if s[i] < 0:
        print("-")
        exit()
    elif s[i] > 0:
        print("+")
        exit()
print(0)
