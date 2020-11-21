#!/usr/bin/env python3

def main():
    n = int(input())
    S = input()
    t = ''
    for s in S:
        t += s
        if t[- 3:] == 'fox':
            t = t[:-3]
    print(len(t))


if __name__ == "__main__":
    main()
