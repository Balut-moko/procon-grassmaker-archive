#!/usr/bin/env python3

def main():
    N = int(input())

    ans = [0] * (N + 1)

    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 100):
                f = x * x + y * y + z * z + x * y + y * z + z * x
                if f < N + 1:
                    ans[f] += 1
    ans.remove(0)
    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
