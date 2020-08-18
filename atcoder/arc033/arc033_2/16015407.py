def main():
    NA, NB = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    union = A | B
    intersection = A & B
    Jaccard = len(intersection) / len(union)
    print(Jaccard)


if __name__ == "__main__":
    main()
