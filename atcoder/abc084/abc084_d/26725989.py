from sys import stdin


def list_primes(limit) -> list:
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False

    return primes


primes = set(list_primes(10**5))
like_num = [0] * (10**5 + 1)
for i in range(1, 10**5 + 1):
    if (i in primes) and ((i + 1) // 2) in primes:
        like_num[i] += like_num[i - 1] + 1
    else:
        like_num[i] += like_num[i - 1]

readline = stdin.readline
q = int(readline())
for _ in range(q):
    l, r = map(int, readline().split())
    print(like_num[r] - like_num[l - 1])
