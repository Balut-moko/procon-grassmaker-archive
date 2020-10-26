#!/usr/bin/env python3

def main():
    cnt = 0
    for i in range(12):
        s = input()
        if 'r' in s:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
