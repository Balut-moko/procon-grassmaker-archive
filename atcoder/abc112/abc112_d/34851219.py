from sys import stdin


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


readline = stdin.readline
n, m = map(int, readline().split())

divs = make_divisors(m)

for val in reversed(divs):
    if m // val >= n:
        ans = val
        break
print(val)
