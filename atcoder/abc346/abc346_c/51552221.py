N, K = map(int, input().split())
A = list(map(int, input().split()))
AA = {a for a in A if a <= K}
ans = K * (K + 1) // 2
ans -= sum(AA)

print(ans)
