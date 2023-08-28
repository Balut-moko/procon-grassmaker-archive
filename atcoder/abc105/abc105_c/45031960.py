from sys import stdin

readline = stdin.readline
n = int(readline())
ans = []
if n == 0:
    print(0)
    exit()

while n != 0:
    m = n % 2
    if m < 0:
        m += 2
    n = (n - m) // (-2)
    ans.append(m)
print(*ans[::-1], sep="")
