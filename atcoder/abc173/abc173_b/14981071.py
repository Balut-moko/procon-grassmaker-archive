#!/usr/bin/env python3

def main():
    N = int(input())
    S = [input() for i in range(N)]

    print("AC x {}".format(S.count('AC')))
    print("WA x {}".format(S.count('WA')))
    print("TLE x {}".format(S.count('TLE')))
    print("RE x {}".format(S.count('RE')))


if __name__ == "__main__":
    main()
