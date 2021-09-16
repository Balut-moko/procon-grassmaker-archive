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


def digit_sum(n):
    return sum(map(int, str(n)))


readline = stdin.readline
n = int(readline())
ans = 'Not Prime'
if n == 1:
    ans = 'Not Prime'
elif len(factorization(n)) == 1 and factorization(n)[0][1] == 1:
    ans = 'Prime'
elif n % 2 != 0 and n % 5 != 0 and digit_sum(n) % 3 != 0:
    ans = 'Prime'

print(ans)
