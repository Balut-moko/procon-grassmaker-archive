N = int(input())
S = input()

cur = 0
ans = 1
while cur < N:
    if S[cur] == "/":
        i = 1
        while True:
            if cur - i < 0:
                break
            if cur + i >= N:
                break
            if S[cur - i] != "1" or S[cur + i] != "2":
                break
            ans = max(ans, 2 * i + 1)
            i += 1
    cur += 1

print(ans)
