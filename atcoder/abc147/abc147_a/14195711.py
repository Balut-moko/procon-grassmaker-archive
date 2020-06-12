#!/usr/bin/env python3

def main():
    A1, A2, A3 = map(int, input().split())
    A=A1+A2+A3
    if A >=22:
        ans='bust'
    else:
        ans='win'
    print(ans)
    
if __name__ == "__main__":
    main()
