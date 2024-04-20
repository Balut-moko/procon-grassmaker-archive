N, Q = map(int, input().split())
T = list(map(lambda x: int(x) - 1, input().split()))

H = [1] * N

for t in T:
    H[t] ^= 1

print(sum(H))
