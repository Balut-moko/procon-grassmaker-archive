from sys import stdin

mod = 1000000007


def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        x %= mod
        n //= 2

    return (K * x) % mod


readline = stdin.readline
n, k = map(int, readline().split())
if n == 1:
    ans = k
else:
    ans = k * (k - 1)
if 3 <= n:
    ans *= pow_k(k - 2, n - 2)
    ans %= mod
print(ans)
