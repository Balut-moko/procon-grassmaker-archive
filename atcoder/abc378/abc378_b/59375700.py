N = int(input())
collect = dict()
for i in range(N):
    q, r = map(int, input().split())
    collect[i + 1] = (q, r)

Q = int(input())
for i in range(Q):
    t, d = map(int, input().split())
    q, r = collect[t]
    if d % q == r:
        print(d)
    else:
        n = (d + q - r) // q
        print(r + q * n)
