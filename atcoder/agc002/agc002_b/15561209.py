#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    xy = [list(map(int, input().split())) for i in range(M)]
    box = [1] * N
    red_flag = [0] * N
    red_flag[0] = 1
    ans = 0
    for i in range(M):
        if red_flag[xy[i][0] - 1] == 1:
            red_flag[xy[i][1] - 1] = 1
        box[xy[i][0] - 1] -= 1
        if box[xy[i][0] - 1] == 0:
            red_flag[xy[i][0] - 1] = 0
        box[xy[i][1] - 1] += 1
    print(sum(red_flag))


if __name__ == "__main__":
    main()
