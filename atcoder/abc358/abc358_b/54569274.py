N, A = map(int, input().split())
T = list(map(int, input().split()))
nxt = 0

for t in T:
    if nxt <= t:
        print(t + A)
        nxt = t + A
    else:
        print(nxt + A)
        nxt += A
