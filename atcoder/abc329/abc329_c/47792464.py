N = int(input())
S = input()

cnt = [0] * 26
pre = S[0]
tmp = 0
for i in range(N):
    if pre == S[i]:
        tmp += 1
    else:
        idx = ord(pre) - ord("a")
        cnt[idx] = max(cnt[idx], tmp)
        tmp = 1
    pre = S[i]

idx = ord(pre) - ord("a")
cnt[idx] = max(cnt[idx], tmp)


print(sum(cnt))
