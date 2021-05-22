#!/usr/bin/env python3

def main():
    s = input()
    s = s.replace('6', 't')
    s = s.replace('9', '6')
    s = s.replace('t', '9')
    print(s[::-1])


if __name__ == "__main__":
    main()
