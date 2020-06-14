#!/usr/bin/env python3

def main():
    X,N = map(int, input().split())
    p = list(map(int, input().split()))
    
    if X not in p:
        ans=X
    else:
        for i in range(100):
            if X-i not in p:
                ans=X-i
                break
            elif X+i not in p:
                ans=X+i
                break
        
    print(ans)
    
if __name__ == "__main__":
    main()
