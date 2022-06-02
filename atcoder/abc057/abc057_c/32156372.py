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
n = int(readline())
divs = make_divisors(n)
ans = 100
for div in divs:
    ans = min(ans, max(len(str(div)), len(str(n // div))))
print(ans)
