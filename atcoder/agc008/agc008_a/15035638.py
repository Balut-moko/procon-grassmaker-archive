def main():
    x, y = map(int, input().split())
    A = abs(abs(x) - abs(y))

    if x * y > 0:
        if x < y:
            B = 0
        else:
            B = 2
    elif x == 0:
        if x < y:
            B = 0
        else:
            B = 1
    elif y == 0:
        if x < y:
            B = 0
        else:
            B = 1
    else:
        B = 1

    print(A + B)


if __name__ == "__main__":
    main()
