from collections import defaultdict


def factorization(n: int):
    di = defaultdict(int)
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            di[i] += cnt

    if temp != 1:
        di[temp] = 1

    if not di:
        di[n] = 1

    return di


A, B = map(int, input().split())
fac = factorization(A)

MOD = 998244353
isEven = True if B % 2 == 0 else False

res = B % MOD
for v in fac.values():
    if v % 2 == 1:
        isEven = True
    res *= (v * B + 1) % MOD
    res %= MOD

if isEven:
    res = res * pow(2, -1, MOD)
else:
    res = (res - 1) * pow(2, -1, MOD)

print(res % MOD)
