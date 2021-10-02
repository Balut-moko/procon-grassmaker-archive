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
n, p = map(int, readline().split())
ans = 1
for val in factorization(p):
    if n <= val[1]:
        ans *= val[0]**(val[1] // n)
print(ans)
