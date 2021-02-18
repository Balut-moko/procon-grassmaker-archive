from itertools import groupby


def rle_list(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, str(len(list(v)))))
    return res


def main():
    S = input()
    ans = [0] * len(S)
    compressed = rle_list(S)
    tmp = 0
    for rl, i in compressed:
        i = int(i)
        if rl == 'R':
            tmp += i
            ans[tmp - 1] += i - i // 2
            ans[tmp] += i // 2
        else:
            ans[tmp - 1] += i // 2
            ans[tmp] += i - i // 2
            tmp += i

    print(*ans)


if __name__ == "__main__":
    main()
