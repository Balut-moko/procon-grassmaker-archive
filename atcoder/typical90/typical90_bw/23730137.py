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
fac = factorization(n)
balls = sum([x[1] for x in fac])
if balls == 1:
    ans = 0
else:
    ans = 1
while 2**ans < balls:
    ans += 1
print(ans)
