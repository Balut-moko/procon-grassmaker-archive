from sys import stdin
from itertools import combinations


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
k = int(readline())

arr = make_divisors(k)

ans = 0
n = len(arr)
for a in range(n):
    for b in range(a, n):
        if k // arr[a] < arr[b]:
            continue
        if k % (arr[a] * arr[b]) != 0:
            continue
        if arr[b] <= k // (arr[a] * arr[b]):
            ans += 1

print(ans)
