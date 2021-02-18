def main():
    S = input()
    ans = [0] * len(S)
    left, right = 0, 0
    tmp0, tmp1 = 0, 0
    rl = S.index('RL')
    while left < len(S):
        if S[left] == 'R':
            if left % 2 == 0:
                tmp0 += 1
            else:
                tmp1 += 1
            left += 1
        else:
            rl = left - 1
            if rl % 2 == 1:
                tmp0, tmp1 = tmp1, tmp0
            right = left
            while right < len(S):
                if S[right] == 'L':
                    if (right - rl) % 2 == 0:
                        tmp0 += 1
                    else:
                        tmp1 += 1
                    right += 1
                else:
                    break
            ans[left - 1] = tmp0
            ans[left] = tmp1
            tmp0, tmp1 = 0, 0
            left = right
    print(*ans)


if __name__ == "__main__":
    main()
