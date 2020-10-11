#!/usr/local/bin python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    state = 0
    tmp = a[0]
    ans = 1
    for i in range(n):
        if state == 0:
            if a[i] - tmp > 0:
                state = 1
            elif a[i] - tmp < 0:
                state = -1
        elif state == 1:
            if a[i] - tmp < 0:
                state = 0
                ans += 1
        elif state == -1:
            if a[i] - tmp > 0:
                state = 0
                ans += 1
        tmp = a[i]

    print(ans)


if __name__ == "__main__":
    main()
