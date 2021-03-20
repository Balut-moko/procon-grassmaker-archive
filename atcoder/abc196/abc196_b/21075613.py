#!/usr/bin/env python3

def main():
    x = input()
    if '.' in x:
        ans = x[:x.find('.')]
    else:
        ans = x

    print(ans)


if __name__ == "__main__":
    main()
