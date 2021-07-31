from sys import stdin


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


readline = stdin.readline
n = int(readline())
ans = [None] * n
ans[0] = 1
for i in range(1, n):
    fac = factorization(i + 1)
    ans[i] = sum([val[1] for val in factorization(i + 1)]) + 1

print(*ans)
