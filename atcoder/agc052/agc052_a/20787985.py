def main():
    t = int(input())
    ans = []
    cases = [[int(input()), input() * 2, input() * 2, input() * 2] for _ in range(t)]
    for case in cases:
        ans.append('0' * case[0] + '1' * case[0] + '0')
    print('\n'.join(ans))


if __name__ == "__main__":
    main()
