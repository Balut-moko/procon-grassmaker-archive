#!/usr/bin/env python3

def main():
    cookies = list(map(int, input().split()))
    ans = 'No'
    for i in range(2**4):
        eat = 0
        not_eat = 0
        for j in range(4):
            if ((i >> j) & 1) == 1:
                eat += cookies[j]
            else:
                not_eat += cookies[j]
        if eat == not_eat:
            ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()
