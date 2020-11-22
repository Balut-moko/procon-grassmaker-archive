#!/usr/bin/env python3

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        ans = 0
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        ans = 1
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        ans = 1
    elif(r1 + c1) & 1 == (r2 + c2) & 1:
        ans = 2
    else:
        ans = 3
        for i in range(-3, 4):
            for j in range(-3, 4):
                r3 = r1 + i
                c3 = c1 + j
                if abs(i) + abs(j) <= 3:
                    if abs(r3 - r2) + abs(c3 - c2) <= 3:
                        ans = 2
                    elif r3 + c3 == r2 + c2 or r3 - c3 == r2 - c2:
                        ans = 2

    print(ans)


if __name__ == "__main__":
    main()
