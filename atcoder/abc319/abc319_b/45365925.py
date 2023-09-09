from sys import stdin

readline = stdin.readline
n = int(readline())


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


divs = make_divisors(n)
divs = [v for v in divs if 1 <= v <= 9]
ans = [1]
for i in range(1, n + 1):
    for j in divs:
        for k in range(1, 1001):
            if i == n // j * k:
                ans.append(j)
                break
        else:
            continue
        break
    else:
        ans.append("-")

print(*ans, sep="")
