#!/usr/bin/env python3

def main():
    A, B = map(int, input().split())
    if A>9 or B>9:
        ans=-1
    else:
        ans=A*B
    print(ans)
    
if __name__ == "__main__":
    main()
