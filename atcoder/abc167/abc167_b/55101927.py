A, B, C, K = map(int, input().split())
ans = 0
ans += min(K, A)
K = max(K - A, 0)
K = max(K - B, 0)
ans -= K

print(ans)
