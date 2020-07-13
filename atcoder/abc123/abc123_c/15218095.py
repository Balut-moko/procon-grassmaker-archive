#!/usr/bin/env python3

def main():
    N = int(input())
    City = [int(input()) for i in range(5)]
    cnt = (N-1)//min(City)+5
    print(cnt)


if __name__ == "__main__":
    main()
