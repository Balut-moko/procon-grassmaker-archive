N = int(input())
A = list(map(int, input().split()))
mod = 998244353
inv_n = pow(N, -1, mod)
p = inv_n
res = 0
for a in A:
    res += p * a
    res %= mod
    p += p * inv_n
    p %= mod
print(res)
