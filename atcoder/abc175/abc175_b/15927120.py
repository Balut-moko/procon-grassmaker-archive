#!/usr/bin/env python3

def main():
    N = int(input())
    L = sorted(map(int, input().split()), reverse=True)
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if L[i] != L[j] and L[i] != L[k] and L[j] != L[k]:
                    if L[i] < L[j] +L[k]:
                        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
