#!/usr/bin/env python3

def main():
    n = int(input())
    for a in range(1, 100):
        for b in range(1, 100):
            if 3**a + 5**b == n:
                print(a, b)
                break
        else:
            continue
        break
    else:
        print(-1)


if __name__ == "__main__":
    main()
