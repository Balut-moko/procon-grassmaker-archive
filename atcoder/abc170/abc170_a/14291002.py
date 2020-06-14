#!/usr/bin/env python3

def main():
    x = list(map(int, input().split()))
    for i,data in enumerate(x):
        if data==0:
            ans=i+1
            break
    print(ans)
    
if __name__ == "__main__":
    main()
