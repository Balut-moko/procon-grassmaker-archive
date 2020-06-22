#!/usr/bin/env python3

def main():
    K = int(input())
    S = input()
    if len(S) > K:
        ans = S[:K] + '...'
    else:
        ans = S
    print(ans)

if __name__ == "__main__":
    main()
