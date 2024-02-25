import itertools


def convert(s, di):
    res = 0
    digit = len(s) - 1
    if di[s[0]] == 0:
        return -1
    for k in s:
        res += di[k] * 10**digit
        digit -= 1
    return res


S1 = input()
S2 = input()
S3 = input()
alphabet = sorted(set(S1 + S2 + S3))
ZeroNine = [i for i in range(10)]

if len(alphabet) > 10:
    print("UNSOLVABLE")
    exit()


for nums in itertools.permutations(ZeroNine, len(alphabet)):
    # 各文字についての対応表を作る
    di = {}
    for i, c in enumerate(alphabet):
        di[c] = nums[i]
    # 対応表に基づき、数式を作る
    N1 = convert(S1, di)
    N2 = convert(S2, di)
    N3 = convert(S3, di)
    if min(N1, N2, N3) <= 0:
        continue
    if N1 + N2 == N3:
        print(N1, N2, N3, sep="\n")
        exit()
print("UNSOLVABLE")
