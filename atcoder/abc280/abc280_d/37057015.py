from collections import defaultdict
from sys import stdin


def factorization(n):
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


readline = stdin.readline
k = int(readline())

di = factorization(k)
ans = 0
for key, val in di.items():
    tmp = 0
    while val > 0:
        tmp += key
        x = tmp
        while x % key == 0:
            x //= key
            val -= 1
    ans = max(ans, tmp)
print(ans)
