#!/usr/bin/env python3

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S) - len(T) + 1):
        cnt = 0
        for j in range(len(T)):
            if S[i + j] == T[j]:
                cnt += 1
        ans = max(ans, cnt)
    print(len(T) - ans)


if __name__ == "__main__":
    main()
