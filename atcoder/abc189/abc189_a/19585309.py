#!/usr/bin/env python3

def main():
    s = input()

    print('Won' if s[0] == s[1] == s[2] else 'Lost')


if __name__ == "__main__":
    main()
