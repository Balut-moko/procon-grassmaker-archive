from sys import stdin

readline = stdin.readline
t = int(readline())

for _ in range(t):
    n, k = map(int, readline().split())
    s = readline()[:-1]

    m = 0
    for i in range(n):
        if s[i] == "1":
            m += 1
    num0 = 0
    num1 = 0
    for i in range(k):
        if s[i] == "0":
            num0 += 1
        if s[i] == "1":
            num1 += 1
    cnt = 0
    if num0 == 0 and num1 == m:
        cnt += 1
    for i in range(n - k):
        if s[i] == "0":
            num0 -= 1
        if s[i] == "1":
            num1 -= 1
        if s[i + k] == "0":
            num0 += 1
        if s[i + k] == "1":
            num1 += 1
        if num0 == 0 and num1 == m:
            cnt += 1
    if cnt == 1:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
