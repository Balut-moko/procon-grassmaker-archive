#!/usr/bin/env python3

def main():
    N = input()
    cnt = 0
    for n in N:
        cnt += int(n)
    if cnt % 9 == 0:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
