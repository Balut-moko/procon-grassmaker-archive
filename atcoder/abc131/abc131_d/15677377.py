#!/usr/bin/env python3

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[1])
    work = 0
    ans = 'Yes'
    for i in range(N):
        work += AB[i][0]
        if work > AB[i][1]:
            ans = 'No'
            break
    print(ans)


if __name__ == "__main__":
    main()
