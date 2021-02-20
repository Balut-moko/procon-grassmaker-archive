#!/usr/bin/env python3

def main():
    S = input()
    ans = 'Yes'
    for i, s in enumerate(S):
        if i % 2 == 0 and s.islower():
            continue
        elif i % 2 == 1 and s.isupper():
            continue
        else:
            ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()
