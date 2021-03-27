#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1 << 60
    for i in range(2**(n - 1)):
        tmp_li = []
        tmp = 0
        for j in range(n - 1):
            if (i >> j) & 1:
                tmp_li.append(a[tmp:j + 1])
                tmp = j + 1
        tmp_li.append(a[tmp:])
        ans_li = []
        for val in tmp_li:
            tmp = val[0]
            for v in val:
                tmp = v | tmp
            ans_li.append(tmp)
        ans_tmp = ans_li[0]
        if 1 < len(ans_li):
            for i in range(1, len(ans_li)):
                ans_tmp = ans_tmp ^ ans_li[i]
        ans = min(ans, ans_tmp)

    print(ans)


if __name__ == "__main__":
    main()
