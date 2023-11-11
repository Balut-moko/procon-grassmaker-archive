from itertools import accumulate


N, Q = map(int, input().split())
S = input()
A = [1 if S[i] == S[i + 1] else 0 for i in range(N - 1)]
cs = list(accumulate(A, initial=0))


for _ in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())
    print(cs[r] - cs[l])
