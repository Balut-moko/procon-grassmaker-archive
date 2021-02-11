def main():
    n = int(input())
    children = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        b = int(input())
        children[b].append(i + 2)

    def calc_saraly(p):
        if len(children[p]) == 0:
            return 1
        else:
            minP, maxP = 10**9, 0
            for child in children[p]:
                P = calc_saraly(child)
                minP = min(minP, P)
                maxP = max(maxP, P)
            return minP + maxP + 1

    print(calc_saraly(1))


if __name__ == "__main__":
    main()
