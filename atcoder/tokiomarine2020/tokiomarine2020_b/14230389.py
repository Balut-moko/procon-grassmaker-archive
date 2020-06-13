#!/usr/bin/env python3

def main():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T =int(input())
    AB = abs(A-B)
    if V < W:
        ans='NO'
    elif AB <= (V-W)*T:
        ans='YES'
    else:
        ans='NO'
    print(ans)
    
if __name__ == "__main__":
    main()
