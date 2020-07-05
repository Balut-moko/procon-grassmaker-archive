#!/usr/bin/env python3

def main():
    import itertools
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    ans = 0
    for i in range(H + 1):
        for j in range(W + 1):
            for n in itertools.combinations(list(range(H)), i):
                for m in itertools.combinations(list(range(W)), j):
                    count = 0
                    for a in n:
                        for b in m:
                            if C[a][b] == "#":
                                count += 1
                    if count == K:
                        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
