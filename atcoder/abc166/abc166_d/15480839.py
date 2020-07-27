import collections


def main():
    X = int(input())
    A, B = 0, 0
    for i in range(-120, 120):
        if A == 0 and B == 0:
            for j in range(-120, 120):
                if i ** 5 - j ** 5 == X:
                    A, B = i, j
                    break
        else:
            break

    print("{} {}".format(A, B))


if __name__ == "__main__":
    main()
