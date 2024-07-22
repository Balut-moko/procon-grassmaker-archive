N = int(input())

if N == 1:
    print(0)
    exit()

N -= 1
d = 1

while True:
    x = (d + 1) // 2
    if N <= 9 * pow(10, x - 1):
        s = list(str(pow(10, x - 1) + N - 1).ljust(d))
        for i in range(x, d):
            s[i] = s[d - 1 - i]
        print("".join(s))
        exit()
    else:
        N -= 9 * pow(10, x - 1)
        d += 1
