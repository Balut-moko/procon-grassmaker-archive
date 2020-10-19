def main():
    a, b = map(int, input().split())
    ans = 'Draw'
    if a != b:
        if a == 1:
            ans = 'Alice'
        elif b == 1:
            ans = 'Bob'
        elif a>b :
            ans = 'Alice'
        else:
            ans = 'Bob'
    print(ans)


if __name__ == "__main__":
    main()
