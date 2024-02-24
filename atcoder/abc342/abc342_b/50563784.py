N = int(input())
P = list(map(int, input().split()))
di = {v: i for i, v in enumerate(P)}
Q = int(input())

for _ in range(Q):
    A, B = map(int, input().split())
    if di[A] < di[B]:
        print(A)
    else:
        print(B)
