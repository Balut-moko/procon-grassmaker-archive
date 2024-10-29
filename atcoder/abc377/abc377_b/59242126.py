S = [input() for _ in [0] * 8]

trans = list(zip(*S))


def check(i, j):
    if "#" in S[i]:
        return False
    if "#" in trans[j]:
        return False
    return True


ans = 0
for i in range(8):
    for j in range(8):
        ans += check(i, j)

print(ans)
