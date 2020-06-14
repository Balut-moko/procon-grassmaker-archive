#!/usr/bin/env python3

def main():
    X,Y = map(int, input().split())
    for i in range(X+1):
        j = X-i
        if 2*i+4*j==Y:
            ans='Yes'
            break
    else:
        ans='No'
    print(ans)
    
if __name__ == "__main__":
    main()
