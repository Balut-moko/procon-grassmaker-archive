import itertools


def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    p_list = list(itertools.permutations(range(1, n + 1)))
    print(abs(p_list.index(p) - p_list.index(q)))


if __name__ == "__main__":
    main()
