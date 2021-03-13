#!/usr/bin/env python3

def main():
    n, m, q = map(int, input().split())
    wv = [list(map(int, input().split()))for _ in range(n)]
    wv = sorted(wv, key=lambda x: x[1], reverse=True)
    x = list(map(int, input().split()))
    for i in range(q):
        left, right = map(int, input().split())
        left -= 1
        right -= 1
        tmp_x = sorted(x[:left] + x[right + 1:])
        tmp_x_in = [False] * len(tmp_x)
        ans = 0
        for w, v in wv:
            for i in range(len(tmp_x)):
                if tmp_x_in[i]:
                    continue
                else:
                    if w <= tmp_x[i]:
                        ans += v
                        tmp_x_in[i] = True
                        break
        print(ans)


if __name__ == "__main__":
    main()
