import itertools


def runLengthEncode(s):
    return [(k, len(list(v))) for k, v in itertools.groupby(s)]


def runLengthDecode(li):
    li = [c * int(n) for c, n in li]
    return "".join(li)


N, K = map(int, input().split())
S = input()

rle = runLengthEncode(S)

ans = []
left = []
right = []
flag = False
for c, n in rle:
    if K > 1:
        left.append((c, n))
        if c == "1":
            K -= 1
    elif K == 1 and c == "0":
        right.append((c, n))
    elif K == 1 and not flag and c == "1":
        flag = True
        left.append((c, n))
    else:
        right.append((c, n))

ans = left + right
print(runLengthDecode(ans))
