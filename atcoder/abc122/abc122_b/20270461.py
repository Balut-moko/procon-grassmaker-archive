def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    S = input()
    ans = 0
    tmp = 0
    for s in S:
        if s == 'A' or s == 'C' or s == 'G' or s == 'T':
            tmp += 1
            ans = max(ans, tmp)
        else:
            tmp = 0

    print(ans)


if __name__ == "__main__":
    main()
