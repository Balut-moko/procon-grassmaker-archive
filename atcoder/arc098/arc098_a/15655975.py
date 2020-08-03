import collections


def main():
    N = int(input())
    S = input()
    cnt = collections.Counter(S)
    E_cnt = cnt['E']
    W_cnt = cnt['W']
    tmp = 0
    if S[0] == 'E':
        E_cnt -= 1
    ans = E_cnt
    for i in range(1, N):
        if S[i] == 'E':
            E_cnt -= 1
        else:
            W_cnt -= 1
        if S[i - 1] == 'W':
            tmp += 1
        ans = min(ans, tmp + E_cnt)

    print(ans)


if __name__ == "__main__":
    main()
