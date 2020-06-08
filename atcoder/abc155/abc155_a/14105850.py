A,B,C = map(int,input().split())
if A==B and A==C:
  print('No')
elif A!=B and A!=C and B!=C:
  print('No')
else:
  print('Yes')
