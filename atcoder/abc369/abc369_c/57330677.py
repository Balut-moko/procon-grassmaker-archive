import itertools

N = int(input())
A = list(map(int, input().split()))
B = [A[i] - A[i - 1] for i in range(1, N)]
ans = N
for k, v in itertools.groupby(B):
    c = len(list(v))
    ans += c * (c + 1) // 2
print(ans)
